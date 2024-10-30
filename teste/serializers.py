from rest_framework import serializers
from teste import models

class ClientSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=18)

    class Meta:
        model = models.Client
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sale
        fields = '__all__'