from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from decimal import *
import math

# Create your views here.
from .models import Receipt, Item
from .serializers import ReceiptSerializer

class ReceiptList(generics.ListCreateAPIView):
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        queryset = Receipt.objects.all()
        return queryset
    
    
class ReceiptDetail(APIView):
    def get(self, request, id, *args, **kwargs):
        receipt = get_object_or_404(Receipt, id=id)
        #serializer = ReceiptSerializer(receipt)
        
        points = 0.00
        
        #First rule
        for ch in receipt.retailer:
            if (ch.isalnum()):
                points+=1
        
        #Second rule
        if (receipt.total % Decimal(1) == 0):
            points+=50
            
        if receipt.total % Decimal(0.25) == 0:
            points += 25
        
        #Third rule
        all_items = receipt.items.all()
        points += (len(all_items) // 2) * 5
        
        #Fifth rule
        for item in all_items:
            description_length = len(item.shortDescription.strip())
            if description_length % 3 == 0:
                points += math.ceil(float(item.price) * 0.2)
        
        #Sixth rule 
        if receipt.purchaseDate.day % 2 == 1:
            points += 6
        
        #Seventh rule 
        if 14 <= receipt.purchaseTime.hour < 16:
            points += 10

        return Response({"Total Points": points})