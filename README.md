# csv2po

[![MIT License](https://img.shields.io/github/license/tomchen/csv2po)](https://github.com/tomchen/csv2po/blob/master/LICENSE "MIT License")

csv2po.py: Python Script to generate gettext .po file from CSV files and vice versa

## Usages

* `exec()`: generate `2_dev/`, `3_i18n/`, `4_prod/` folders
* `generateDevAndI18n()`: generate `2_dev/`, `3_i18n/` folders
* `generateProd()`: generate `4_prod/` folder (`2_dev/`, `3_i18n/` exist)
* `generateDevOnly()`: generate `2_dev/` folder

## Settings

See [settings.py](https://github.com/tomchen/csv2po/blob/master/settings.py)

## Folders

(default folder names)

* `0_source`: source folder
* `1_template`: template folder
* `2_dev`: development folder
* `3_i18n`: gettext i18n (localization) files (`.po`, `.mo`, `.pot`) folder
* `4_prod`: production folder

## Projects using this library

* [MM678 I18N](https://github.com/might-and-magic/mm678-i18n) Might and Magic games (6-8 & merge) localization project