"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog

from django.conf.urls import handler404, handler500
from panel.views import handler404

urlpatterns = [
    path('cp/', admin.site.urls),
    
    # inclusión de urls de panel
    # path('', include('panel.urls')),
    path('panel/', include('panel.urls')),
    path('', include('blog.urls')),
    
]

handler404 = 'panel.views.handler404' 

admin.site.index_title = 'Sitio de Administración'
admin.site.site_header = 'Panel de Administración'
admin.site.site_title = 'Ficticia Inc.'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)