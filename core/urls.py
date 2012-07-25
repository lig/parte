from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^profile/posts$', 'profile_posts', name='profile-posts'),
)
