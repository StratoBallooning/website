from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch import index


class BlogPage(Page):
    date = models.DateField('Post Date')
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title', icon='title')),
        ('paragraph', blocks.RichTextBlock(icon='doc-full')),
        ('image', ImageChooserBlock(icon='image')),
    ])

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []
