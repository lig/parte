from django.conf.urls import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
    url(r'^users/((?P<user_id>\w+))$', 'profile', name='profile'),
    url(r'^users/((?P<user_id>\w+))/posts$', 'profile_posts',
        name='profile-posts'),
    url(r'^posts/new$', 'posts_new', name='posts-new'),
    url(r'^posts/(?P<post_id>\w+)$', 'posts_post', name='posts-post'),
)
