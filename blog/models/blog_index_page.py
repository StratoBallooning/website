from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index

from blog.models.blog_page import BlogPage


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    @property
    def blogs(self):
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request):
        blogs = self.blogs

        context = super(BlogIndexPage, self).get_context(request)
        context['blogs'] = blogs

        return context
