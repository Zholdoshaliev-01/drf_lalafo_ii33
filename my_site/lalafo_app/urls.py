from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet
from django.urls import path, include


router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
