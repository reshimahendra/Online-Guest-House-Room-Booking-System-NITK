# Generated by Django 2.1.1 on 2018-10-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_transactions_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='no_people_done',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]