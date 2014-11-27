from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
# import photologue
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prmtools.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$',"django.views.static.serve", {"document_root":settings.MEDIA_ROOT,},),
    url(r'^photologue/', include("photologue.urls", namespace='photologue')),
)
