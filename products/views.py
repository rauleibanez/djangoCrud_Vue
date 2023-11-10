# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        #--- FILTRADO POR CATEGORIA ---
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        #--- FILTRADO POR NOMBRE Y DESCRIPCION ---
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(description__icontains=search) 
        return queryset    
    # --------------------------------------------
    # Para filtrar productos desde las categorias 
    # --> /api/products/by_category/?category=3
    # --------------------------------------------
    #@action(detail=False)
    #def by_category(self, request):
    #    category = self.request.query_params.get('category', None)
    #    products = Product.objects.filter(category=category)
    #    serializer = ProductSerializer(products, many=True)
    #    return Response(serializer.data)
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# -------------------------------------------------
# Cuando se trabaja con generics de rest_framework
# se deben crear estas dos clases por cada modelo
# -------------------------------------------------
"""
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
"""
