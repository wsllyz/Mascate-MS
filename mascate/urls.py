from django.contrib import admin
from django.urls import path

from principal.views import home
from funcionario.views import adms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('adms/', adms),
]
