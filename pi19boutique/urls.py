"""pi19boutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import index, usuario, produto, produto_favoritar, editar, excluir

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
	path('index/', index, name='index'),
	path('usuario/', usuario, name='usuario'),
    path('produto/', produto, name='produto'),
    path('produto/<int:id>/favoritar/', produto_favoritar, name='produto_favoritar'),
    path('editar/<int:id>/', editar, name="editar"),
    path('excluir/<int:id>/', excluir, name="excluir"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

