# Generated by Django 4.1 on 2023-03-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_bank_transcations_pay_voucher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_transcations',
            name='pay_voucher',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bank_transcations',
            name='rec_voucher',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]