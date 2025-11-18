# AuthApp/urls.py

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

# ESTA LÍNEA ES ESENCIAL: Asigna la lista de URLs generadas a la variable que Django espera.
urlpatterns = router.urls