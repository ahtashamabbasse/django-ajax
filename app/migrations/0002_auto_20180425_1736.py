# Generated by Django 2.0.3 on 2018-04-25 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='name',
            new_name='title',
        ),
    ]
