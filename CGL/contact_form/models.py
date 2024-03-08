from django import forms
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from CGL.base.block import BaseStreamBlock 

##### CONTACT PAGE FORMS #####
class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    https://docs.wagtail.org/en/stable/reference/contrib/forms/index.html
    """

    page = ParentalKey("ContactPage", related_name="form_fields", on_delete=models.CASCADE)

class ContactPage(AbstractEmailForm):
    
    gallery = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField(BaseStreamBlock(), use_json_field=True)
    ty_response = RichTextField(blank=True)
    template = "contact_form/contact_page.html"
    
    map_api = models.CharField(max_length=1000, blank=True, null=True)
    # Note how we include the FormField object via an InlinePanel using the
    # related_name value
    
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("body"),
        InlinePanel("form_fields", heading="Form fields", label="Field"),
        FieldPanel("ty_response"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email",
        ),
    ]
    settings_panels = [
        FieldPanel("gallery"),
        FieldPanel("map_api"),
    ]