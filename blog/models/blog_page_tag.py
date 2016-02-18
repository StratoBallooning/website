from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('blog.BlogPage', related_name='blog_pages')
