# Generated by Django 5.0.2 on 2024-03-07 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='map_api',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
