# Generated by Django 5.0.2 on 2024-03-04 15:01

import CGL.about_page.models
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_page', '0004_alter_aboutuspage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspage',
            name='body',
            field=wagtail.fields.StreamField([('About_Section', wagtail.blocks.StructBlock([('about_title', wagtail.blocks.CharBlock(required=False)), ('about_block', wagtail.blocks.RichTextBlock(icon='pilcrow', required=False, template='blocks/paragraph_block.html')), ('gallery', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link_title', wagtail.blocks.TextBlock(required=False)), ('link_page', wagtail.blocks.PageChooserBlock(required=False))])), ('About_Section_Extended', wagtail.blocks.StructBlock([('about_title', wagtail.blocks.CharBlock(required=False)), ('about_block', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('block_quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock()), ('attribute_name', wagtail.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks', icon='media', template='blocks/embed_block.html'))], required=False))])), ('Lab_section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.TextBlock(required=False)), ('readmore_title', wagtail.blocks.CharBlock(required=True)), ('readmore_link', wagtail.blocks.PageChooserBlock(required=True))])), ('Price_Table', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('description_z', wagtail.blocks.TextBlock(required=True))])), ('ProgressSection', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))])), ('ServicesSection', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('view_link', wagtail.blocks.PageChooserBlock(required=False)), ('cards', wagtail.blocks.ListBlock(CGL.about_page.models.ServiceCardBlock, required=False))])), ('TestimonialsSections', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False))]))], blank=True, use_json_field=True, verbose_name='Page Body'),
        ),
    ]
