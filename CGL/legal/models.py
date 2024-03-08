from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail import blocks

class LegalInformation(blocks.StructBlock):
    text_title = blocks.TextBlock(required=False)
    details = blocks.RichTextBlock(required=False)
    list = blocks.RichTextBlock(required=False)
    
    class Meta:
        template = "legal/legal_text.html"
        
class LegalPage(Page):
    template = "legal/legal_index.html"
    max_count = 4
    gallery = models.ForeignKey(
      "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Landscape mode only; horizontal width between 1000px and 3000px.",
    )
    title_legal = models.CharField(max_length=255, blank=True, null=True)
   
    body = StreamField([
        ('Legal_Infromation', LegalInformation()),
        ], verbose_name="Content", blank=True, use_json_field=True
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("title"),
        
        MultiFieldPanel([
            FieldPanel("body"),    
        ], "Description",
        ),
        
    ]
    settings_panels = [
        FieldPanel("gallery")
    ] 
