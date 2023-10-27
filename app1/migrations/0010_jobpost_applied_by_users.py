# Generated by Django 4.2 on 2023-09-16 06:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0009_alter_jobpost_education_alter_jobpost_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='applied_by_users',
            field=models.ManyToManyField(blank=True, related_name='applied_jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]