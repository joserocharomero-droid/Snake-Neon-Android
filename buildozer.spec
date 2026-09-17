[app]
title = Snake Neon
package.name = snakeneon
package.domain = org.snakegame

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,wav,ogg,mp3
version = 1.0.0

requirements = python3,pygame

orientation = landscape
# La interfaz usa un lienzo lógico 1000x700 y controles táctiles grandes.
android.allow_backup = True
fullscreen = 1

android.permissions = INTERNET
android.archs = arm64-v8a
android.api = 34
android.minapi = 21
android.build_tools = 34.0.0
android.accept_sdk_license = True
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1