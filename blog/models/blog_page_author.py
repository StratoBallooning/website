from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from modelcluster.fields import ParentalKey


class BlogPageAuthor(Orderable, models.Model):
    blog_page = ParentalKey('BlogPage', related_name='contributors')
    user = models.ForeignKey(User)
    position = models.CharField(max_length=64, default='Author')

    panels = [
        FieldPanel('user'),
        FieldPanel('position'),
    ]
