from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=80, default="")
    sub_category = models.CharField(max_length=80, default="")
    description = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='shop/images', default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name
