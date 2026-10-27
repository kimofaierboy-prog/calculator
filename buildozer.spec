[app]
title = calculator_kimo
package.name = calculator
package.domain = org.karem
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,json
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.api = 36
android.ndk = 29
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
