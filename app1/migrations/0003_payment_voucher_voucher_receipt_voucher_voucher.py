# Generated by Django 4.1 on 2022-12-22 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_payment_voucher_receipt_voucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_voucher',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher'),
        ),
        migrations.AddField(
            model_name='receipt_voucher',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher'),
        ),
    ]