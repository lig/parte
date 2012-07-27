from django.conf import settings

from forms import PostForm


def post_form(request):
    return {'post_form': request.user.is_authenticated() and PostForm()}


def site(request):
    return {'SITE': settings.SITE}
