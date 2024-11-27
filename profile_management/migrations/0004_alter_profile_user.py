# Generated by Django 5.1.1 on 2024-11-02 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0009_remove_user_groups_remove_user_is_staff_and_more'),
        ('profile_management', '0003_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login_register.user'),
        ),
    ]
