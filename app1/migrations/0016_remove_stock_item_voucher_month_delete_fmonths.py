# Generated by Django 4.1 on 2023-02-16 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_stock_item_voucher_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_item_voucher',
            name='month',
        ),
        migrations.DeleteModel(
            name='fmonths',
        ),
    ]
