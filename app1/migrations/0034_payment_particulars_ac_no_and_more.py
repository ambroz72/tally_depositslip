# Generated by Django 4.1 on 2023-03-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0033_payment_particulars'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_particulars',
            name='ac_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment_particulars',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment_particulars',
            name='ifscode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment_particulars',
            name='inst_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment_particulars',
            name='inst_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payment_particulars',
            name='transcation_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
