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
# SDK & NDK paths (diset via workflow)
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

# API settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# build-tools versi stabil
android.build_tools_version = 33.0.2
android.accept_sdk_license = True

# optional: biar lebih stabil
p4a.branch = master
