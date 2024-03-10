from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    PageChooserBlock
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock 

class ImageBlock(StructBlock):
    """
    Custom `StructBlock` for utilizing images with associated caption and
    attribution data
    """

    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blocks/image_block.html"


class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """

    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"

class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(blank=True, required=False, label="e.g. Mary Berry")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"

# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(
        icon="pilcrow", template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        template="blocks/embed_block.html",
    )


class AboutSection (StructBlock):
    about_title = CharBlock(required=False)
    about_block = RichTextBlock(icon="pilcrow", template="blocks/paragraph_block.html",required=False)
    gallery = ImageChooserBlock(required=False)
    link_title = TextBlock(required=False)
    link_page = PageChooserBlock(required=False)
    
    class Meta:
        template = "includes/isAbout.html"

class CleanSection(StructBlock):
    about_title = CharBlock(required=False)
    about_block = BaseStreamBlock(required=False)
     
    class Meta:
        template = "includes/isAbout_noImage.html" 

class CarouselManager(StructBlock):
    gallery_list = ImageBlock(required=False)
    
    class Meta:
        icon = "gallery-list"
        template = "blocks/image_block.html"

class ServiceParallaxBlock(StructBlock):
    services_image = ImageChooserBlock(required=False)     
    services_title = TextBlock(required=False)
    services_link = PageChooserBlock(required=False)
    
    class Meta:
        icon = "Parralax-img-list"

class ServiceCardBlock(StructBlock):
    card_title = CharBlock(required=False)
    card_description = BaseStreamBlock(required=False)
    service_1_img = ImageChooserBlock(required=False)
    card_link = PageChooserBlock(required=False)
    class Meta:
        icon = "placeholder"

class QLCardBlock(StructBlock):
    ql_title = CharBlock(required=False)
    ql_description = BaseStreamBlock(required=False)
    ql_link = PageChooserBlock(required=False)
    class Meta:
        icon = "quicklinks_list"
        
class CarouselSlider(StructBlock):
    
    title = CharBlock(required=True)
    description = TextBlock(required=False)
    
    gallery = ImageChooserBlock(required=False)
    
    page_link_title_standard = CharBlock(required=False)
    page_link = PageChooserBlock(required=False)

    page_link_title_secondary = CharBlock(required=False)
    page_link_2 = PageChooserBlock(required=False)

    class Meta:
        icon = "sliders"

class QuickLinksSection(StructBlock):
    
    featured_page_title = TextBlock(required=False)
    page_description = CharBlock(required=False)
    page = PageChooserBlock(required=False)
    
    class Meta: 
        icon = "quicklinks-x"
class TestimonialsSection(StructBlock):
    fullname= TextBlock(required=True)
    client_type= TextBlock(required=False)
    comment= CharBlock(required=True)

    class Meta:
        icon = "testimonials"

class ContactSection (StructBlock):
    title = CharBlock(required=False)
    phone = CharBlock(required=False)
    suggestion = CharBlock(required=False)
   
    class Meta:
        template = "includes/contact_block.html"
   