# Generated by Django 5.1.1 on 2024-10-20 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pet_type', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('fish', 'Fish'), ('bird', 'Bird'), ('hamster', 'Hamster'), ('rabbit', 'Rabbit'), ('guinea_pig', 'Guinea Pig'), ('turtle', 'Turtle'), ('lizard', 'Lizard'), ('snake', 'Snake'), ('frog', 'Frog'), ('parrot', 'Parrot'), ('chinchilla', 'Chinchilla'), ('ferret', 'Ferret'), ('hedgehog', 'Hedgehog'), ('horse', 'Horse'), ('goat', 'Goat')], max_length=20)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('adoption_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='pets/main/')),
                ('time_in_shelter', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pets/gallery/')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pet_listing.pet')),
            ],
        ),
    ]
