from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.wagtailsearch import index
from modelcluster.contrib.taggit import ClusterTaggableManager

from .blog_index_page import BlogIndexPage
from .blog_page_tag import BlogPageTag


class BlogPage(Page):
    subtitle = models.CharField(max_length=100, blank=True)
    date = models.DateField('Post Date')
    intro = models.CharField(max_length=250, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title', icon='title', template='blog/blocks/heading_block.html')),
        ('paragraph', blocks.RichTextBlock(icon='pilcrow')),
        ('image', ImageChooserBlock(icon='image', template='blog/blocks/image_block.html')),
    ])

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('date'),
        InlinePanel('contributors', label='Contributors', min_num=1),
        StreamFieldPanel('body'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
        ImageChooserPanel('feed_image'),
        FieldPanel('intro'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []

    @property
    def blog_index(self):
        return self.get_ancestors().type(BlogIndexPage).last()
