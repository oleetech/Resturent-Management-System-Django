# Generated by Django 4.2.5 on 2023-10-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0016_orderinfo_billed_orderinfo_cookfinish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brtable',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
