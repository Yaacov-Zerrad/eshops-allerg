from itertools import product
from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import ProductSerializer


class MyOrderItemSerializer(serializers.Serializer):
    product = ProductSerializer
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )
        

class MyOrderSerializer(serializers.Serializer):
    items = MyOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            'first_name',
            "last_name",
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'items',
            "paid_amount"
        )


class OrderItemSerializer(serializers.Serializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            'first_name',
            "last_name",
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'items',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
        
        
        