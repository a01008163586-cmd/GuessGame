[app]

# (str) Title of your application
title = SmartGuess

# (str) Package name
package.name = smartguess

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ahmedali

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required.
android.minapi = 21

# (str) Android NDK version you want to use
android.ndk = 25b

# (str) Android SDK Build-Tools version to use (مهم جداً لتفادي خطأ 37)
android.sdk_build_tools_version = 33.0.2

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True


#
# Buildozer section
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
