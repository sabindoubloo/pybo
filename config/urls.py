from django.contrib import admin
from django.urls import path, include
from pybo import views
from pybo.views import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),
]
handler404 = 'common.views.page_not_found'
