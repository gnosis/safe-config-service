# Generated by Django 4.2.3 on 2023-08-14 15:24

import gnosis.eth.django.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chains", "0037_chain_hidden"),
    ]

    operations = [
        migrations.AddField(
            model_name="gasprice",
            name="max_fee_per_gas",
            field=gnosis.eth.django.models.Uint256Field(
                blank=True, null=True, verbose_name="Max fee per gas (wei)"
            ),
        ),
        migrations.AddField(
            model_name="gasprice",
            name="max_priority_fee_per_gas",
            field=gnosis.eth.django.models.Uint256Field(
                blank=True, null=True, verbose_name="Max priority fee per gas (wei)"
            ),
        ),
    ]
