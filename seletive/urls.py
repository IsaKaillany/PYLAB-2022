# Roteamento da aplicação

from django.contrib import admin
from django.urls import path, include

#função path gerencia roteamentos dentro da aplicação
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls'))
]
