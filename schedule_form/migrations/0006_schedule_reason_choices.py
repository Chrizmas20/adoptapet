# Generated by Django 5.1.1 on 2024-11-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_form', '0005_schedule_cancelled_schedule_upcoming'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='reason_choices',
            field=models.CharField(choices=[('duplicate_request', 'Duplicate Request'), ('not_picking_up', 'Not Picking Up Pet on Time'), ('overwhelmed_adopter', 'Overwhelmed Adopter'), ('ethical_safety_concerns', 'Ethical or Safety Concerns'), ('inability_to_meet_needs', 'Inability to Meet Pet’s Needs')], max_length=50, null=True),
        ),
    ]
