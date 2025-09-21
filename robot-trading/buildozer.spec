[app]
# Nama aplikasi
title = Robot Trading

# Nama package (tanpa spasi, huruf kecil semua)
package.name = robottrading

# Domain package (bebas, bisa pakai org.example)
package.domain = org.example

# Folder source code
source.dir = .

# File yang di-include
source.include_exts = py,png,jpg,kv,atlas

# Versi aplikasi
version = 0.1

# Requirements (wajib python3 + kivy, bisa ditambah sesuai kebutuhan)
requirements = python3,kivy

# Orientasi layar
orientation = portrait

# 0 = tidak fullscreen, 1 = fullscreen
fullscreen = 0


[buildozer]
# Level log
log_level = 2

# Jangan build sebagai root
warn_on_root = 1

# Platform target
target = android
