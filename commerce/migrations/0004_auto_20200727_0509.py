# Generated by Django 3.0.8 on 2020-07-27 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ShippingAddress1',
            new_name='billingAddress1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingCity',
            new_name='billingCity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingCountry',
            new_name='billingCountry',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingName',
            new_name='billingName',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ShippingPostcode',
            new_name='billingPostcode',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='bilingAddress1',
            new_name='shippingAddress1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='bilingCity',
            new_name='shippingCity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='bilingCountry',
            new_name='shippingCountry',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='bilingName',
            new_name='shippingName',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='bilingPostcode',
            new_name='shippingPostcode',
        ),
    ]
