# Generated by Django 5.1.1 on 2024-09-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_user_details_user_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_detail',
            name='district',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
