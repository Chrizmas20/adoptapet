# Generated by Django 5.1.1 on 2024-11-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_form', '0003_alter_schedule_adopter'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
