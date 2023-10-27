# Generated by Django 4.2 on 2023-09-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
