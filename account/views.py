from django.conf import settings
from django.apps import apps
from django.views.generic import DetailView

class UserProfileView(DetailView):

    model = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    template_name = 'user_profile.html'
