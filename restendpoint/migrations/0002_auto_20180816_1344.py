# Generated by Django 2.1 on 2018-08-16 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restendpoint', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickup',
            old_name='long',
            new_name='longitude',
        ),
    ]