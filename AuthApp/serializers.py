# AuthApp/serializers.py

from rest_framework import serializers
from .models import Products 
# Asegúrate de que 'Products' es el nombre correcto de tu modelo en models.py

# El nombre de esta clase debe ser *exactamente* ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'