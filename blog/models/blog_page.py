from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch import index


class BlogPage(Page):
    date = models.DateField('Post Date')
    intro = models.CharField(max_length=250)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
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
        StreamFieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + [
        ImageChooserPanel('feed_image'),
        FieldPanel('intro'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []
