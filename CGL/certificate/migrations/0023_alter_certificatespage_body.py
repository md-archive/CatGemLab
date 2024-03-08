# Generated by Django 5.0.2 on 2024-03-06 23:01

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0022_certificateslist_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatespage',
            name='body',
            field=wagtail.fields.StreamField([('CertificateSearch', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))]))], blank=True, use_json_field=True, verbose_name='Builder'),
        ),
    ]