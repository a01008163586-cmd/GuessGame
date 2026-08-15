import json
import random
from pathlib import Path

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.metrics import dp

from game import Game


class GuessGameApp(App):

    title = "خَمّن الحاجة - أحمد علي عيسى"

    def build(self):
        self.game = Game()

        root = BoxLayout(
            orientation="vertical",
            padding=dp(14),
            spacing=dp(9)
        )

        title = Label(
            text="🧠 خَمّن الحاجة",
            font_size=dp(28),
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(title)

        developer = Label(
            text="تم تطوير اللعبة بواسطة أحمد علي عيسى",
            font_size=dp(14),
            size_hint_y=None,
            height=dp(32)
        )
        root.add_widget(developer)

        self.status = Label(
            font_size=dp(17),
            halign="center"
        )

        self.status.bind(
            size=lambda *_:
            setattr(self.status, "text_size", self.status.size)
        )

        root.add_widget(self.status)

        grid = GridLayout(
            cols=2,
            spacing=dp(7),
            size_hint_y=None
        )

        grid.bind(
            minimum_height=grid.setter("height")
        )

        questions = [
            ("🍎 فاكهة", "category", "فاكهة"),
            ("🥕 خضار", "category", "خضار"),
            ("🐾 حيوان", "category", "حيوان"),
            ("🐦 طائر", "category", "طائر"),

            ("🪽 تستطيع الطيران", "can_fly", True),
            ("🌊 تعيش في الماء", "lives_in_water", True),

            ("🐱 لها فرو أو شعر", "has_fur", True),

            ("📏 حجمها كبير", "size", "كبير"),
            ("📏 حجمها صغير", "size", "صغير")
        ]

        for text, key, value in questions:

            button = Button(
                text=text,
                font_size=dp(14),
                size_hint_y=None,
                height=dp(54)
            )

            button.bind(
                on_release=lambda btn,
                k=key,
                v=value,
                t=text:
                self.ask(k, v, t)
            )

            grid.add_widget(button)

        root.add_widget(grid)

        controls = BoxLayout(
            size_hint_y=None,
            height=dp(55),
            spacing=dp(7)
        )

        hint_button = Button(
            text="💡 تلميح",
            font_size=dp(14)
        )
        hint_button.bind(on_release=self.hint)

        guess_button = Button(
            text="🎯 تخمين",
            font_size=dp(14)
        )
        guess_button.bind(on_release=self.guess_popup)

        new_button = Button(
            text="🔄 لعبة جديدة",
            font_size=dp(14)
        )
        new_button.bind(on_release=self.new_game)

        controls.add_widget(hint_button)
        controls.add_widget(guess_button)
        controls.add_widget(new_button)

        root.add_widget(controls)

        self.update()

        return root

    def update(self, message="فكر في حاجة سرية واسألني عن صفاتها 🤫"):

        self.status.text = (
            f"{message}\n\n"
            f"⭐ النقاط: {self.game.score}    "
            f"🔎 الاحتمالات: {len(self.game.possible)}"
        )

    def ask(self, key, value, text):

        result = self.game.ask(key, value)

        if result:
            message = f"{text}\n\n✅ نعم"
        else:
            message = f"{text}\n\n❌ لا"

        self.update(message)

        if len(self.game.possible) == 1:

            answer = self.game.possible[0]["name"]

            self.update(
                f"🤖 أعتقد أنها: {answer}"
            )

    def hint(self, *_):

        hint = self.game.hint()

        self.update(
            "💡 " + hint
        )

    def guess_popup(self, *_):

        box = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(10)
        )

        input_box = TextInput(
            hint_text="اكتب اسم الحاجة",
            multiline=False,
            font_size=dp(18)
        )

        box.add_widget(input_box)

        button = Button(
            text="تأكيد",
            size_hint_y=None,
            height=dp(50)
        )

        box.add_widget(button)

        popup = Popup(
            title="🎯 تخمين",
            content=box,
            size_hint=(0.9, 0.35)
        )

        def submit(_):

            name = input_box.text.strip()

            if not name:
                return

            if self.game.guess(name):

                popup.dismiss()

                self.update(
                    f"🎉 صح!\n"
                    f"الإجابة: {self.game.secret['name']}\n"
                    f"المحاولات: {self.game.attempts}"
                )

            else:

                self.game.score = max(
                    0,
                    self.game.score - 10
                )

                popup.dismiss()

                self.update(
                    "❌ التخمين غير صحيح.\n"
                    "خسرت 10 نقاط."
                )

        button.bind(
            on_release=submit
        )

        popup.open()

    def new_game(self, *_):

        self.game.start()

        self.update()


if __name__ == "__main__":
    GuessGameApp().run()
