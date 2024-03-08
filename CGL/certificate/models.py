from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, MultipleChooserPanel
from wagtail.blocks import ListBlock, StructBlock, CharBlock
from wagtail.fields import StreamField
from CGL.base.block import ImageChooserBlock, HeadingBlock, RichTextBlock
from wagtail.snippets.models import register_snippet
from wagtail.search import index


class CertificateSearch(StructBlock):
    title = CharBlock(required=False)
    class Meta:
        template = "certificate/certificates_search.html"

class GenTable(StructBlock):
    title = CharBlock(max_length=255, required=False)
    textfield = RichTextBlock(required=False)
    class Meta:
        icon = "table_generator"

class TableForImages(StructBlock):
    images = ListBlock(ImageChooserBlock(), required=False)
    class Meta:
        icon = "images_list"

class CertificatesList(Page):
    template= "certificate/report_response.html"
    gallery = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    images = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    date_pub_title = models.CharField(max_length=100, blank=True, null=True)
    date_published = models.DateField("Date of publication: ", blank=True, null=True)
    cert_id_title = models.CharField(max_length=100, blank=True, null=True)
    
    body = StreamField([
        ("Table_Generator", GenTable()),
        ("Image_Inserter", TableForImages()),
    ], blank=True, null=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("cert_id_title"),
        MultiFieldPanel([
            FieldPanel("date_pub_title"),
            FieldPanel("date_published"),  
        ], "Fecha de Publicación" ),
        MultiFieldPanel([
            FieldPanel("body"),
        ], "Contenido" ),
        
    ]
    search_fields = Page.search_fields + [
        index.SearchField("body"),
        index.SearchField("cert_id_title"),
        index.SearchField("date_published"),
        
    ]
    settings_panels = [
        FieldPanel("gallery"),
    ] 
    
    parent_page_types = ["CertificatesPage"] 
    subpage_types = []

class CertificatesPage(Page):
    template = "certificate/certificates.html"
    gallery = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField([
        ('CertificateSearch', CertificateSearch())
    ], verbose_name="Builder", blank=True, use_json_field=True)
    content_panels = Page.content_panels + [
        FieldPanel("body"), 
    ]
    settings_panels = [
        FieldPanel("gallery"),
    ]
    subpage_types = ["CertificatesList"]