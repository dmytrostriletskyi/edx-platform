# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0003_auto_20151217_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='currency',
            field=models.CharField(default=b'tzs', help_text='Lower-case ISO currency codes', max_length=8),
        ),
        migrations.AlterField(
            model_name='invoicetransaction',
            name='currency',
            field=models.CharField(default=b'tzs', help_text='Lower-case ISO currency codes', max_length=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(default=b'tzs', max_length=8),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='currency',
            field=models.CharField(default=b'tzs', max_length=8),
        ),
    ]