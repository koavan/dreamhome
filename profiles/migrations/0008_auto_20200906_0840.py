# Generated by Django 2.2.5 on 2020-09-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20200906_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='noname', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]