from rest_framework import serializers
from cars.models import Car
from cars.models import Category


class CategoriesAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'date']


class CarAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'color', 'model', 'cat_id', 'registration_no', 'date']
