# Generated by Django 4.2.4 on 2023-08-23 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0003_university_campuses_delete_cases'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='University_Campuses',
            new_name='UniversityCampus',
        ),
    ]