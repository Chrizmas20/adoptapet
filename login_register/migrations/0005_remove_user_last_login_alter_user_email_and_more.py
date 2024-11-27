# Generated by Django 5.1.1 on 2024-11-02 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0004_user_last_login_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]