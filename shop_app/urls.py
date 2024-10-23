from django.urls import path, include
from rest_framework import routers
from shop_app.views import *

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product-detail/', ProductDetailListCreateView.as_view(), name='product-detail'),
    path('product-detail/<int:pk>/', ProductDetailListCreateView.as_view(), name='product-detail'),
    path('protected/', ProtectedDataView.as_view(), name='protected-data'),
]
