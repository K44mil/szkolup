# Generated by Django 2.2.1 on 2019-06-03 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0005_auto_20190603_1720'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mark',
            new_name='Rate',
        ),
    ]
