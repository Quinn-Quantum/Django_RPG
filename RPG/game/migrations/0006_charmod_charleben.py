# Generated by Django 3.2.9 on 2021-11-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20211125_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='charmod',
            name='charLeben',
            field=models.IntegerField(null=True),
        ),
    ]