# Generated by Django 4.2.2 on 2023-06-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sum',
            field=models.IntegerField(default=0),
        ),
    ]
