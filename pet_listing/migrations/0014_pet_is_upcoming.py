# Generated by Django 5.1.1 on 2024-11-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_listing', '0013_pet_is_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='is_upcoming',
            field=models.BooleanField(default=False),
        ),
    ]
