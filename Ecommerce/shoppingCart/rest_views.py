from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.authentication import  TokenAuthentication
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import  SearchFilter,OrderingFilter


from shoppingCart.models import Orders,Products,Orders_items
from shoppingCart.serializers import UserSerializer,ProductSerializer,OrdersSerializer,Order_items_Serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # search_fields = ('id', 'title')
    # filter_backends = [SearchFilter,OrderingFilter]


class OrdersViewset(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def list(self, request):
        order_obj =Orders.objects.filter(user_id = request.user)
        serializer = OrdersSerializer(order_obj, many=True)
        return Response(serializer.data)

    def create(self, request,  *args, **kwargs):
        data = request.data
        new_order = Orders.objects.create(user_id=request.user,total=data['total'],status=data['status'],mode_of_payment=data['mode_of_payment'])
        new_order.save()

        for product in data['products']:
            product_obj =Products.objects.get(title=product['title'])
            new_order.products.add(product_obj)
        serializer = OrdersSerializer(new_order)

        return Response(serializer.data)


    def retrive(self, request, pk=None):
        queryset = Orders.objects.filter(pk=pk,user_id=request.user, )
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = OrdersSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)



    # def partial_update(self, request, pk=None):
    #     orders= Orders.objects.get(user_id=request.user,pk=pk)
    #     data = request.data
    #
    #     try:
    #         for product in data['products']:
    #             product_obj = Products.objects.get(title=product['title'])
    #             # products = Products.objects.get(title=data['title'])
    #             orders.products = product_obj
    #     except Exception:
    #         print('error',Exception)
    #
    #     orders.total =data.get('total',orders.total)
    #     orders.status = data.get('status', orders.status)
    #     orders.mode_of_payment = data.get('mode_of_payment', orders.mode_of_payment)
    #     orders.save()
    #
    #     serialized = OrdersSerializer(request.user, data=request.data, partial=True)
    #     return Response(serialized.data,status=status.HTTP_202_ACCEPTED)





class Order_item_Viewset(viewsets.ModelViewSet):
    queryset = Orders_items.objects.all()
    serializer_class = Order_items_Serializer
    authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        data = request.data
        print(data['product_id'])
        print(data['quantity'])
        newProduct = Products.objects.get(title=data['product_id'])
        newProduct.save()
        new_order_item = Orders_items.objects.create(product_id=newProduct,quantity=data['quantity'])
        new_order_item.save()
        serializer = Order_items_Serializer(new_order_item)
        return Response(serializer.data)











