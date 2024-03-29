# Generated by Django 2.2.5 on 2020-05-28 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('LAND-APPROVED', 'LAND-APPROVED'), ('LAND-UNAPPROVED', 'LAND-UNAPPROVED'), ('BUILDING', 'BUILDING')], max_length=50)),
                ('area_sqft', models.FloatField()),
                ('area_cents', models.FloatField()),
                ('facing_direction', models.CharField(max_length=30)),
                ('land_rate_sqft', models.FloatField()),
                ('land_rate_cent', models.FloatField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('NOT-AVAILABLE', 'NOT-AVAILABLE'), ('NOT-FOR-SALE', 'NOT-FOR-SALE'), ('SOLD', 'SOLD')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('located_at', models.TextField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('area_sqft', models.FloatField()),
                ('area_cents', models.FloatField()),
                ('total_properties', models.IntegerField()),
                ('properties_occupied', models.IntegerField(blank=True, null=True)),
                ('properties_available', models.IntegerField()),
                ('land_rate_sqft', models.BigIntegerField()),
                ('land_rate_cent', models.BigIntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('NOT-AVAILABLE', 'NOT-AVAILABLE')], max_length=30)),
                ('approved', models.BooleanField(default=False)),
                ('approval_body', models.CharField(blank=True, choices=[('PANCHAYAT', 'PANCHAYAT'), ('DTCP', 'DTCP')], max_length=20, null=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Owner')),
            ],
            options={
                'verbose_name_plural': 'Sites',
            },
        ),
        migrations.CreateModel(
            name='SiteImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='proprepo.Site')),
            ],
            options={
                'verbose_name_plural': 'SiteImages',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='proprepo.Property')),
            ],
            options={
                'verbose_name_plural': 'PropertyImages',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='site_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprepo.Site'),
        ),
    ]
