# Generated by Django 4.0.3 on 2022-03-27 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_demo_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demo',
            old_name='response',
            new_name='result',
        ),
    ]
