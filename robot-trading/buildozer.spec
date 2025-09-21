[app]
# Nama aplikasi yang tampil di Android
title = Robot Trading

# Nama package (unik, jangan sama dengan app lain)
package.name = robottrading
package.domain = org.robottrading

# Versi aplikasi
version = 0.1

# Folder source code
source.dir = .

# File yang disertakan dalam build
source.include_exts = py,png,jpg,kv,atlas,json,txt

# Entry point (file utama Python)
main.py = main.py

# Requirements Python (tambahkan kalau ada lagi)
requirements = python3,kivy,requests

# Orientasi aplikasi
orientation = portrait

# Mode fullscreen (1 = fullscreen, 0 = tidak)
fullscreen = 0

# Icon dan splash (opsional, bisa ganti gambar sendiri)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Permissions Android
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Jika app butuh storage (opsional)
# android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Minimum Android API
android.minapi = 21

# Target Android API (biar update, default 33 atau 34)
android.api = 33

# SDK/NDK
android.ndk = 23b
android.ndk_api = 21

# Nama output apk
package.version_name = 0.1
package.version_code = 1


[buildozer]
# Level log
log_level = 2
warn_on_root = 1

# Direktori output
bin_dir = bin

# Jangan hapus file build
use_cache = 1
