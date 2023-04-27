from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from menu.views import Menu


urlpatterns = [
 path('admin/', admin.site.urls),
 path('', Menu, name='index'),
 path('__debug__/', include('debug_toolbar.urls')),
 re_path(r'^(.*)/$', Menu, name='index')
]
