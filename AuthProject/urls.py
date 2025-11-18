# AuthProject/urls.py

from django.contrib import admin
from django.urls import path, include
# No debes importar 'AuthApp.urls' directamente aquí, solo usar include()

urlpatterns = [
    path('admin/', admin.site.urls),
    # DEBE USAR 'include()' para cargar el archivo AuthApp/urls.py
    path('api/', include('AuthApp.urls')), 
]