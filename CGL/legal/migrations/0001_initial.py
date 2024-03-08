# Generated by Django 5.0.2 on 2024-03-03 18:33

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('title_legal', models.CharField(blank=True, max_length=255, null=True)),
                ('body', wagtail.fields.StreamField([('Legal_Infromation', wagtail.blocks.StructBlock([('text_title', wagtail.blocks.TextBlock(required=False)), ('details', wagtail.blocks.RichTextBlock(required=False)), ('list', wagtail.blocks.RichTextBlock(required=False))]))], blank=True, use_json_field=True, verbose_name='Content')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
