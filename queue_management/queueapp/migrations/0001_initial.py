# Generated by Django 5.1.4 on 2024-12-08 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=6)),
                ('registration_start_time', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('current_count', models.IntegerField(default=0)),
                ('details', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=10)),
                ('aadhaar_no', models.CharField(max_length=12)),
                ('dob', models.DateField()),
                ('position', models.IntegerField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queueapp.line')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]