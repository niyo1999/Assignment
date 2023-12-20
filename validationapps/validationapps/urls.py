from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('validations.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns=[ 
            re_path(r'healthchecks/', include('django_healthchecks.urls')),
            path('admin/', admin.site.urls),
            path('', include('validations.urls')),
            
            ]
