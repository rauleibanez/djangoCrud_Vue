# ------------------------------------------------
# Este archivo se usa para serializar objetos y 
# poder pasarlos como objetos Json además 
# configura el set de datos para realizar filtrado
# por campos
# ------------------------------------------------
from rest_framework import serializers
from .models import Product, Category
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    category = filters.NumberFilter(Field_name='Category', lookup_expr='exact')
    name = filters.CharFilter(Field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {
            'category':['exact'],
            'name':['icontains'],
        }

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    price_type_description = serializers.ReadOnlyField(source='get_price_type_display')

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'description', 'price', 'category', 'category_name', 'price_type', 'price_type_description')
        filterset_class = ProductFilter
        #fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
