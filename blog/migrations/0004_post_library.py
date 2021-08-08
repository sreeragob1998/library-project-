# Generated by Django 3.2.6 on 2021-08-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='library',
            field=models.CharField(choices=[('M', 'Homme'), ('F', 'Femme')], default='M', max_length=1),
        ),
    ]