# Generated by Django 5.0.7 on 2024-07-16 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitorlog',
            name='visitor_id',
        ),
    ]
