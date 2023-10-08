from django.contrib import admin
from django.urls import path, include
from autenticacao import views
urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('registro/', include('registro.urls')),
    path('visualizacao/', include('visualizacao.urls')),
    path('base/', include('base.urls')),

]
