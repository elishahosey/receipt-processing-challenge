from rest_framework import serializers
from .models import Item, Receipt

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['shortDescription', 'price']

class ReceiptSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = ['id','retailer', 'purchaseDate', 'purchaseTime', 'total', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        receipt = Receipt.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(receipt=receipt, **item_data)
        return receipt


