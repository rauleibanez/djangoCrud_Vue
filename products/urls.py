from django.urls import path 
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename = 'products') 
router.register(r'categories', CategoryViewSet, basename = 'categories') 

urlpatterns = router.urls