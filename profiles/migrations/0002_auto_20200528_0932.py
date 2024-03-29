# Generated by Django 2.2.5 on 2020-05-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='email_id',
            new_name='support_email_id',
        ),
        migrations.AlterField(
            model_name='owner',
            name='company_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='contact_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
