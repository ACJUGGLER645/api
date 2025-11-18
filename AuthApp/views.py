# AuthApp/views.py

from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    # Obtiene todos los objetos Products
    queryset = Products.objects.all()
    # Usa el serializador que creamos
    serializer_class = ProductSerializer