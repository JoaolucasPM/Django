# Generated by Django 5.1.1 on 2024-10-01 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]