"""
[3] Explain what does django-admin.py make messages command is used for?

The django-admin.py make-messages command is used in Django to facilitate the process of creating or updating translation message files for internationalization (i18n) and localization (l10n) of a Django project.

Here's a breakdown of its purpose and usage:

[i]Internationalization (i18n):

Purpose: Django supports the internationalization of applications, allowing developers to create versions of their projects in multiple languages.

How it Works: Developers mark strings in their Python code and templates as translatable using the gettext function. These marked strings are called "translation strings."

Translation Message Files: To manage translations, Django uses special files known as translation message files (.po files). These files contain pairs of original (English) strings and their translated versions in different languages.

[ii]make-messages Command:

Purpose: The make-messages command is used to generate or update these translation message files based on the marked translation strings in the source code.

Usage: The command is typically run from the project's root directory using the following syntax:

django-admin.py makemessages -l <language_code>

Compilation (Optional):

After translations are added to the .po files, the translations need to be compiled into binary .mo files for Django to use them efficiently.

django-admin.py compilemessages

"""