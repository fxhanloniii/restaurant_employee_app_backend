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
