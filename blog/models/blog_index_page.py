from __future__ import unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from taggit.models import Tag


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
        from .blog_page import BlogPage
        blogs = BlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-date')

        return blogs

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)

        # Get base blog queryset
        blogs = self.blogs

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            blogs = blogs.filter(tags__name=tag)

        # Add tags to context
        context['tags'] = Tag.objects.annotate(pages=models.Count('blogpage')).filter(pages__gte=1)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs, 10)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        # Set blogs on context object
        context['blogs'] = blogs

        return context
