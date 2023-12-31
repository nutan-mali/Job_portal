# Generated by Django 4.2.5 on 2023-10-27 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_rename_required_skills_jobpost_technologies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('msg', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
