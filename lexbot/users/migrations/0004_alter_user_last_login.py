# Generated by Django 3.2.13 on 2022-06-15 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, help_text='last login of user', verbose_name='last_login'),
        ),
    ]
