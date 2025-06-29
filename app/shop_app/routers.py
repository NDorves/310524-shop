# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers
#
# from shop_app import views
# from shop_app.views import *
#
# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet) # маршруты для представл-я CategoryViewSet, исп-я DefaultRouter.
# router.register(r'suppliers', SupplierViewSet)  #маршруты для представления SupplierViewSet, исп. DefaultRouter
# router.register(r'products', ProductViewSet)
# #router.register(r'products', ProductUpdateDeleteView)   #ProductDetailUpdateDeleteView.
# router.register(r'product-detail', ProductDetailViewSet)
# #router.register(r'product-detail', ProductDetailListUpdateDeleteView)
# router.register(r'address', AddressViewSet)
# router.register(r'customer', CustomerViewSet)
# #router.register(r'customer', CustomerDetailUpdateDeleteView)
# router.register(r'order', OrderViewSet)
# #router.register('order', OrderDetailsUpdateDeleteView)
# router.register(r'order-item', OrderItemViewSet)
# #router.register(r'order-item', OrderItemCreateUpdateSerializer)
#
# urlpatterns = {
#     path('', views.hello, name='hello'),
# # #    path('', include(routers.urls)),
#  #   path('products/', ProductDetailViewSet.as_view(), name='products'),  #маршр. для предст-й
# #     path('products/<int:pk>/', ProductUpdateDeleteView.as_view(), name='products'),
# # #   path('product-detail/', ProductDetailListCreateViewSet.as_view(), name='product-detail'),
# #     path('product-detail/<int=pk>/', ProductDetailListUpdateDeleteView.as_view(), name='product-detail'),
# #     path('address/', AddressViewSet.as_view(), name='address'),  # маршруты для представления AddressViewSet
# #  #   path('customer/', CustomerListCreateViewSet.as_view(), name='customer'),
# #     path('customer/<int=pk>/', CustomerDetailUpdateDeleteView.as_view(), name='customer'),
#     # path('order/', OrderListCreateViewSet.as_view()),
#     # path('order/<int=pk>/', OrderListCreateViewSet.as_view(), name='order'),
#     # path('order-item/', OrderItemListCreateViewSet.as_view(), name='order-item'),
#     # path('order-item/<int=pk>/', OrderItemCreateUpdateSerializer.as_view(), name='order-item'),

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
    path('api/register/', RegisterView.as_view(), name='register'),
    path('private/', PrivateView.as_view(), name='private'),
]



