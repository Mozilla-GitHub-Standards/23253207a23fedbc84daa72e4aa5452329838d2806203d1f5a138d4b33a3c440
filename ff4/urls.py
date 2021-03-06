from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    import os
    import django
    urlpatterns += patterns('',
        (r'^static/admin/(?P<path>.*)$',  'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '/admin'}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^debug/500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        (r'^debug/404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
    )

urlpatterns += patterns('things.views',
    (r'^$', 'home'),
    (r'^gallery/$', 'gallery'),
    (r'^gallery/chap/(?P<chapter>\d+)/$', 'gallery_nav'),
    (r'^gallery/chap/(?P<chapter>\d+)/(?P<page>\d+)/$', 'gallery'),
    (r'^gallery/chap/(?P<chapter>\d+)/(?P<featured>featured)$', 'gallery_nav'),
    (r'^gallery/chap/(?P<chapter>\d+)/(?P<page>\d+)/(?P<featured>featured)$', 'gallery'),
    (r'^quiz/$', 'quiz'),
    (r'^collage/$', 'collage'),
    (r'^collage/(?P<slug>\w+)/$', 'collage'),
    (r'^collage/(?P<slug>\w+)/snapshot/$', 'collage_snapshot'),
    (r'^features/$', 'features'),
    (r'^download_reminder/$', 'download_reminder'),
    (r'^robots.txt$', 'robots'),
)
