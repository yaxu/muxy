# Generated by Django 3.1.4 on 2020-12-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_streamnotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='slug',
        ),
    ]
