# Generated by Django 4.2.8 on 2023-12-16 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_sala_konferencyjna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='capacity_hall',
            field=models.IntegerField(default=False),
        ),
    ]
