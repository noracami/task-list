from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^shifttable/', include('shifttable.urls', namespace='shifttable')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'$', 'tasklist.views.home', name='home'),
)
