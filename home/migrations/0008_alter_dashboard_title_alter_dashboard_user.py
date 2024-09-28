# Generated by Django 5.1.1 on 2024-09-28 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_user_id_dashboard_user_dashboard_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='title',
            field=models.CharField(default='User', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
