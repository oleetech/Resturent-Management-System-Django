# Generated by Django 4.2.6 on 2023-10-05 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0008_order_isorder_order_mac_order_menu_item_order_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu_item',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.menuitem'),
        ),
    ]
