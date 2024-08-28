from django.db import models
import uuid

# Create your models here.
class Receipt(models.Model):
    #autogenerate id for the receipt instance
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    retailer=models.CharField(max_length=100)
    purchaseDate=models.DateField()
    purchaseTime=models.TimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
class Item(models.Model):
    #Since there can be multiple items for a receipt, it will need separate model
    receipt = models.ForeignKey(Receipt, related_name='items', on_delete = models.CASCADE)
    shortDescription = models.CharField(max_length = 400)
    price = models.DecimalField(max_digits=10, decimal_places=2)