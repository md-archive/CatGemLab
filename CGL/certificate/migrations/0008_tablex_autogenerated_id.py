# Generated by Django 5.0.2 on 2024-03-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0007_tablex_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablex',
            name='autogenerated_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
