# from django.db import models
from django.contrib.auth.hashers import make_password

from shoppingCart.models import Orders,Products,Orders_items
from rest_framework import serializers, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('getimage_url')
    print('image_url',image_url)
    class Meta:
        model = Products
        fields = ['id',
                    'title' ,
                    'description' ,
                    'price' ,
                    'created_At' ,
                  'updated_At',
                    'image',
                    'image_url'
                    ]
    def getimage_url(self,obj):
        print('obj.image.url',obj.image.url)
        return obj.image.url



class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders

        fields = [
            'id',
        'user_id',
            'total',
            'products',
            'created_At',
            'updated_At',
            'status',
            'mode_of_payment',

        ]
        depth =2





class Order_items_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Orders_items
        fields = [
            'id',

            'product_id',
            'quantity',
            'price',
            'total_cost'
        ]
        depth = 1




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    # def destroy(self,request):
    #     user= User.objects.get(username=request.data.user)
    #     user.delete()












   # def update(self, instance, validated_data):
    #     demo = Orders.objects.get(pk=instance.id)
    #     Orders.objects.filter(pk=instance.id) .update(**validated_data)
    #     return demo