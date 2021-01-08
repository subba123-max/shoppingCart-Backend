from django.conf import settings
from django.urls import path,include
from rest_framework import routers
from django.conf.urls.static import  static

from shoppingCart.rest_views import UserViewSet,ProductViewset,OrdersViewset,Order_item_Viewset
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('account/register', UserViewSet,)
# router.register('account/logout', UserViewSet,)
router.register('product',ProductViewset)
router.register('orders',OrdersViewset,basename="Orders")
router.register('order_items',Order_item_Viewset)
# router.register('register', UserViewSet)




urlpatterns=[
    path('',include(router.urls)),
    path('account/login/',obtain_auth_token),

]



