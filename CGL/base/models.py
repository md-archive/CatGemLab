###### IMPORTING ALL THE LIBRARIES FOR THE MAIN WAGTAIL BASE DIRECTORY #############
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PublishingPanel,
)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.fields import RichTextField, StreamField
from wagtail.models import (
    Collection,
    DraftStateMixin,
    LockableMixin,
    Page,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
    WorkflowMixin,
)
#from wagtail.search import index
from .block import BaseStreamBlock, ImageChooserBlock



##### REGISTERING SETTING **GSC** To control the site contents (header and footer and other type of linkable socials pages and copyright bs) #####3 
@register_setting
class GenericSiteContent(BaseGenericSetting):
    id = models.BigAutoField(primary_key=True)
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    twitter_url = models.URLField(verbose_name="Twitter URL", blank=True)
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    linkedin_url = models.URLField(verbose_name="Linkedin URL", blank=True)
    whatsapp_url = models.URLField(verbose_name= "WhatsApp Url", blank=True)
    
    business_address = models.CharField(verbose_name="Business Address", max_length=100, blank=True)
    business_email = models.EmailField(verbose_name="Business Email", max_length=254, blank=True)
    business_phone = models.CharField(verbose_name="Telephone Number", max_length=15, blank=True)
    business_workhours = models.CharField(verbose_name="Working Hours", max_length=100, blank=True)
    
    footer_description = models.CharField(verbose_name="Description", max_length=255, blank=True)
    footer_copyright_notice = models.CharField(verbose_name="Company Name", max_length=40, blank=True)
    
    whatsapp_title = models.CharField(verbose_name="Texto Llamada", max_length=30, blank=True)
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook_url"),
                FieldPanel("twitter_url"),
                FieldPanel("instagram_url"),
                FieldPanel("linkedin_url"),
            ],
            "Social settings",
        ),
        MultiFieldPanel([
                FieldPanel("whatsapp_title"),
                FieldPanel("whatsapp_url"),
            ], "Contacto Interactivo",
        ),
        MultiFieldPanel(
            [
                FieldPanel("business_address"),
                FieldPanel("business_email"),
                FieldPanel("business_phone"),
                FieldPanel("business_workhours"),
            ],
            "Business Information",
        ),
        MultiFieldPanel(
            [
                FieldPanel("footer_description"),
                FieldPanel("footer_copyright_notice"),
            ],
            "Site Footer Description",
        ),
    ]
    
