# Generated by Django 3.2.6 on 2021-08-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
