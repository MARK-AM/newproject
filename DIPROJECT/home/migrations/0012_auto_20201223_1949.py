# Generated by Django 3.1.4 on 2020-12-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201223_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='ov',
            new_name='overview',
        ),
    ]