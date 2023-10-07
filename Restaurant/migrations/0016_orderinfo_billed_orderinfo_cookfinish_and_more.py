# Generated by Django 4.2.5 on 2023-10-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0015_orderinfo_cookorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='billed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='cookFinish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='served',
            field=models.BooleanField(default=False),
        ),
    ]