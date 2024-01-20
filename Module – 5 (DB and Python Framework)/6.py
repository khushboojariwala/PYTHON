"""
[6] Mention what command line can be used to load data into Django?
-> In Django, you can use the loaddata management command to load data from fixture files into your database. Fixture files are serialized representations of Django models and can be in various formats such as JSON, XML, or YAML.

Here's the basic syntax for using the loaddata command:
python manage.py loaddata <fixture_file>

You can also specify multiple fixture files separated by spaces if you need to load data from multiple sources:
python manage.py loaddata fixture1.json fixture2.json

"""