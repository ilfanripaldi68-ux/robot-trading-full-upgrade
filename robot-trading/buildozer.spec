[app]
title = Robot Trading
package.name = robottrading
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1
requirements = python3,kivy,requests
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# pakai path yang sama dengan yang kita install di workflow
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.api = 33
android.minapi = 21
android.ndk = 25c
android.ndk_api = 21
