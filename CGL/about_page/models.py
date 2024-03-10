from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail import blocks
from CGL.base.block import ImageChooserBlock, BaseStreamBlock, AboutSection, CleanSection, PageChooserBlock, ServiceCardBlock, TestimonialsSection

class LabSection (blocks.StructBlock):
    
    title = blocks.CharBlock(required=True)
    description = blocks.TextBlock(required=False)
    readmore_title = blocks.CharBlock(required=True)
    readmore_link = PageChooserBlock(required=True)
    
    class Meta:
        template = "about_page/isLab.html"
class PriceTable (blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    description_z = blocks.TextBlock(required=True)
    
    class Meta:
        template = "about_page/isPriceTable.html"
class ProgressSection (blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    
    class Meta:
        template = "about_page/isProgress.html"

class ServicesSection (blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    view_link = PageChooserBlock(required=False)
    
    cards = blocks.ListBlock(ServiceCardBlock, required=False)
    
    content_panels = [
        FieldPanel("title"),
        FieldPanel("view_link"),
        InlinePanel("cards", label="Service Cards"),
    ]
    class Meta:
        template = "about_page/isServices.html"

class TestimonialsCardSelector (blocks.StructBlock):
    title = blocks.CharBlock(required=True)    
    section_image = ImageChooserBlock(required=True)
    card = blocks.ListBlock(TestimonialsSection(), required=False)
    
    class Meta:
        template = "about_page/isTestimonials.html"

class AboutUsPage(Page):
    """
    About Us Page
    """
    template = "about_page/about_page.html"

    gallery = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )

    body = StreamField([
        ('About_Section', AboutSection()),
        ('About_Section_Extended', CleanSection()),
        ('ServicesSection', ServicesSection()),
        ('TestimonialsSections', TestimonialsCardSelector()),
        
    ], verbose_name="Page Body", blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([ 
            FieldPanel("body"),
        ], "General Context",     
    ),   
    ]
    settings_panels = [
        FieldPanel("gallery"),
    ]

   
   