# Generated by Django 5.1.1 on 2024-11-03 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0013_alter_user_options_alter_user_managers_and_more'),
        ('profile_management', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login_register.user'),
        ),
    ]