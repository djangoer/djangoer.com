from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    url(r'^cas/', include('mama_cas.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
