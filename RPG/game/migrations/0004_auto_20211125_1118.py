# Generated by Django 3.2.9 on 2021-11-25 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20211125_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charmod',
            name='besigteFeinde',
        ),
        migrations.RemoveField(
            model_name='charmod',
            name='ep',
        ),
        migrations.RemoveField(
            model_name='charmod',
            name='leben',
        ),
        migrations.RemoveField(
            model_name='charmod',
            name='level',
        ),
    ]
