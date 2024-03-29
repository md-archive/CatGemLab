# Generated by Django 5.0.2 on 2024-03-06 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0011_listofcertificates'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofcertificates',
            old_name='t_id',
            new_name='item_title',
        ),
        migrations.AddField(
            model_name='listofcertificates',
            name='item_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collection_snippets', to='wagtailcore.collection'),
        ),
        migrations.AddField(
            model_name='listofcertificates',
            name='item_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
