from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^accounts/', include('registration.urls')),
)
