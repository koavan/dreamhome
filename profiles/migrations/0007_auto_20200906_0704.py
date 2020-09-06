# Generated by Django 2.2.5 on 2020-09-06 07:04

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, unique=True),
        ),
    ]