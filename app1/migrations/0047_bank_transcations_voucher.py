# Generated by Django 4.1.7 on 2023-03-14 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_debit_note_voucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_transcations',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher'),
        ),
    ]
