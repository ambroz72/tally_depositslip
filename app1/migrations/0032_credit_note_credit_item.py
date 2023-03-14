# Generated by Django 4.1 on 2023-02-28 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_remove_credit_note_comp_remove_credit_note_voucher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='credit_note',
            fields=[
                ('screditid', models.AutoField(primary_key=True, serialize=False, verbose_name='cnid')),
                ('credit_no', models.IntegerField(default=1)),
                ('customer', models.CharField(max_length=100, null=True)),
                ('creditdate', models.DateField(null=True)),
                ('ledger_acc', models.CharField(max_length=100, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('subtotal', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('grandtotal', models.CharField(max_length=100, null=True)),
                ('tracking_no', models.CharField(max_length=100, null=True)),
                ('dis_doc_no', models.CharField(max_length=100, null=True)),
                ('dis_thr', models.CharField(max_length=100, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('carrie_nmag', models.CharField(max_length=100, null=True)),
                ('billlr_no', models.CharField(max_length=100, null=True)),
                ('mt_vh_no', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('inv_no', models.CharField(max_length=100, null=True)),
                ('inv_date', models.DateField(null=True)),
                ('mname', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('reg_type', models.CharField(max_length=100, null=True)),
                ('gst_uin', models.CharField(max_length=100, null=True)),
                ('pl_suply', models.CharField(max_length=100, null=True)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.voucher')),
            ],
        ),
        migrations.CreateModel(
            name='credit_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('scredit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.credit_note')),
            ],
        ),
    ]