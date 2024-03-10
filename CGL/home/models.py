from django.db import models
from django.shortcuts import render
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from CGL.base.block import AboutSection, CleanSection, ServiceParallaxBlock, CarouselSlider
from CGL.blog.models import ArticlePage, BlogIndexPage
from wagtail import blocks

class BlogSection(blocks.StructBlock):
    title = blocks.CharBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        
        # Retrieve the BlogIndexPage
        blog_index_page = BlogIndexPage.objects.live().first()

        # If the BlogIndexPage exists, fetch its posts and add to the context
        if blog_index_page:
            context['blog_posts'] = blog_index_page.get_context(context['request']).get('posts', [])

        return context

    class Meta:
        template = "includes/blog_section.html"


class HomeServicesSection (blocks.StructBlock):
    title = blocks.CharBlock(required=False)    
    cards = blocks.ListBlock(ServiceParallaxBlock, required=False)
    
    content_panels = [
        FieldPanel("title"),
        InlinePanel("cards", label="Parallax"),
    ]
    class Meta:
        template = "homepage/isServices.html"


class CarouselSection(blocks.StructBlock):
    
    slider = blocks.ListBlock(CarouselSlider(), required=True)

    content_panels = [
        InlinePanel("slider", label="Slider")    
    ]
    class Meta:
        template = "homepage/isCarousel.html"
       

class QuickLinksSection (blocks.StructBlock):
    
    featured_page_1_title = blocks.TextBlock(required=False)
    page_1_description = blocks.CharBlock(required=False)
    page_1 = blocks.PageChooserBlock(required=False)
    
    featured_page_2_title =blocks.TextBlock(required=False)
    page_2_description = blocks.CharBlock(required=False)
    page_2 = blocks.PageChooserBlock(required=False)
    
    featured_page_3_title = blocks.TextBlock(required=False)
    page_3_description = blocks.CharBlock(required=False)
    page_3 = blocks.PageChooserBlock(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Featured Page 3",
    )
    
    featured_page_4_title = blocks.TextBlock(required=False)
    page_4_description = blocks.CharBlock(required=False)
    page_4 = blocks.PageChooserBlock(required=False)
    
    class Meta:
        template = "homepage/isQL.html"  
        
class ContactSection (blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    phone = blocks.CharBlock(required=False)
    suggestion = blocks.CharBlock(required=False)
    class Meta:
        template = "includes/contact_block.html"
        
class HomePage(Page):
    template = "homepage/home_index_page.html"
     # Body section of the HomePage
    
    body = StreamField([
        ('Carousel_Section', CarouselSection()),
        ('About_Section', AboutSection()),
        ('Clean_Section', CleanSection()),
        ('Services_Section', HomeServicesSection()),
        ('QuickLinks_Section', QuickLinksSection()),
        ('Contact_Section', ContactSection()),
        ('BlogSection', BlogSection()),
    ], verbose_name="Home Body", blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        
        MultiFieldPanel([
            FieldPanel("body"), 
        ], "General Context",     
    ),   
        
    ]
