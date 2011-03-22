

from django.conf import settings
from django.conf.urls.defaults import *

import os

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/openresources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.split(settings.ROOT_PATH)[0], 'openresources/media')}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('openresources.urls')),
)
