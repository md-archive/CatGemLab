from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from modelcluster.fields import ParentalKey 
from CGL.base.block import PageChooserBlock, BaseStreamBlock, ImageChooserBlock, CleanSection
from wagtail import blocks

class Main (blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=False)
    description = BaseStreamBlock(required=False)
    class Meta:
        template = "services_page/isMain.html"

class AccordionFAQ (blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    description = BaseStreamBlock(required=False)
    class Meta:
        template = "services_page/accordion.html"

class ServicesDescription(Page):
    template = "services_page/services_description.html"
    
    body = StreamField([
        ('Main_section', Main()),
        ('Clean_Section', CleanSection()),
        ('FAQ', AccordionFAQ()),
        
    ], verbose_name="Home Body", blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("body"), 
        ], "General Context",     
    ),   
    ]
    
    gallery = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    
    contact_header = models.CharField(max_length=40, null=True, blank=True)
    contact_title = models.CharField(max_length=80, null=True, blank=True)
    contact_link_txt = models.CharField(max_length=80, null=True, blank=True)
    contact_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        verbose_name="contact",
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    settings_panels = Page.settings_panels + [
        MultiFieldPanel([
            FieldPanel("gallery"),
            ], "Site Controls Settings..."
        ),
        MultiFieldPanel([
                FieldPanel("contact_header"),
                FieldPanel("contact_title"),
                FieldPanel("contact_page"),
                FieldPanel("contact_link_txt"),    
            ], "Contact Setting"
        ),
    ]
    
    parent_page_types = ["ServicesIndexPage"] 
    subpage_types = []
    
class ServicesIndexPage(Page):
    template = "services_page/services_index_page.html"
     # Body section of the HomePage
    gallery = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    
    contact_header = models.CharField(max_length=40, null=True, blank=True)
    contact_title = models.CharField(max_length=80, null=True, blank=True)
    contact_link_txt = models.CharField(max_length=80, null=True, blank=True)
    contact_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        verbose_name="contact",
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    body = StreamField([
        ('Main_section', Main()),
    ], verbose_name="Home Body", blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("body"), 
        ], "General Context",     
    ),   
    ]
    settings_panels = Page.settings_panels + [
        MultiFieldPanel([
            FieldPanel("gallery"),
            ], "Site Controls Settings..."
        ),
        MultiFieldPanel([
                FieldPanel("contact_header"),
                FieldPanel("contact_title"),
                FieldPanel("contact_page"),
                FieldPanel("contact_link_txt"),    
            ], "Contact Setting"
        ),
    ]
    
    parent_page_types = [] 
    subpage_types = ["ServicesDescription"]
    def get_services(self):
        # Get all live and public child pages recursively
        return self.get_children().live().public().type(ServicesIndexPage)
   

    def get_context(self, request):
        context = super().get_context(request)
        context['services'] = ServicesIndexPage.objects.child_of(self).live()
        return context