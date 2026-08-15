import json, random
from pathlib import Path

DATA_FILE = Path(__file__).with_name("things.json")

class Game:
    def __init__(self):
        with DATA_FILE.open("r", encoding="utf-8") as f:
            self.things = json.load(f)
        self.start()

    def start(self):
        self.secret = random.choice(self.things)
        self.possible = self.things.copy()
        self.score = 100
        self.attempts = 0
        self.hints = 0

    def ask(self, key, value):
        answer = self.secret[key] == value
        if answer:
            self.possible = [x for x in self.possible if x[key] == value]
        else:
            self.possible = [x for x in self.possible if x[key] != value]
        return answer

    def guess(self, name):
        self.attempts += 1
        return name.strip().casefold() == self.secret["name"].strip().casefold()

    def hint(self):
        self.hints += 1
        self.score = max(0, self.score - 10)
        hints = [
            f"الفئة: {self.secret['category']}",
            f"اللون: {self.secret['color']}",
            f"الحجم: {self.secret['size']}",
            "لها فرو أو شعر." if self.secret["has_fur"] else "ليس لها فرو."
        ]
        return hints[self.hints-1] if self.hints <= len(hints) else "استخدمت كل التلميحات."
