# Generated by Django 5.0.2 on 2024-03-03 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_image_blogindexpage_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepage',
            old_name='image',
            new_name='gallery_images',
        ),
    ]