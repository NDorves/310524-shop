from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
