from django.db import models
import uuid

# Create your models here.
class Products(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_name = models.CharField(max_length=1000)
    vendor = models.CharField(max_length=100)
    mrp = models.FloatField(null=True, blank=True, default=None)
    batch_no = models.IntegerField(null=False)
    batch_date = models.DateTimeField(null=False)
    quantity = models.IntegerField(null=False)
    status = models.IntegerField(null=False)

    class Meta:
        db_table = 'products'