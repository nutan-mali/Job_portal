# Generated by Django 4.2.5 on 2023-10-07 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_rename_description_jobpost_about_the_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='required_skills',
            new_name='technologies',
        ),
    ]
