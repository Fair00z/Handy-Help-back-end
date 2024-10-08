# Generated by Django 5.1.1 on 2024-10-01 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_dashboard_client_dashboard_worker_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=300)),
                ('work_location', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.client')),
            ],
        ),
    ]
