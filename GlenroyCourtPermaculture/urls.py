from django import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from GlenroyCourtPermaculture.views import index
from dashboard.views import report

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index),  
    path('reports/', report),
    path('dashboard/', include('dashboard.urls')),
    path('graphql', include('dashboard.urls')),
    path('summernote/', include('django_summernote.urls')) 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)