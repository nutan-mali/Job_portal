# Generated by Django 4.2.5 on 2023-10-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_jobpost_education_alter_jobpost_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='desc',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
