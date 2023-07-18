from rest_framework import serializers

from .models import *

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = "__all__"

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class OutOfStockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutOfStockItem
        fields = "__all__"

