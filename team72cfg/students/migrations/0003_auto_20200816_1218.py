# Generated by Django 3.0.8 on 2020-08-16 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_skills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]