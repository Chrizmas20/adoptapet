# Generated by Django 5.1.1 on 2024-11-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(default='No message attached', max_length=400),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(default='Unnamed Title', max_length=30),
        ),
    ]
