from rest_framework import serializers
from myapp.models import Quote, Category



class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quote
        fields=["id", "text", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category        
        fields=["id", "category", "created_at", "updated_at"]

