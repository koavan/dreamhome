# Generated by Django 2.2.5 on 2020-06-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='contact_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]