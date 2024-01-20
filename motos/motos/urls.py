"""
URL configuration for motos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.urls import path, include

#Importo para que aparezcan las imagenes
#NOTA: No es recomendable hacerlo en produccion
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('motors.urls')),
    path('items/', include('item.urls')),
    path('dashboard', include('dashboard.urls')),
    path('inbox/', include('chat.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#NOTA: No es recomendable hacerlo en produccion