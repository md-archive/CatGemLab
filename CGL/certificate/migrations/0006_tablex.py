# Generated by Django 5.0.2 on 2024-03-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0005_certificateslist_gallery_certificateslist_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]