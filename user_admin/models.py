from django.db import models


class AdminProduct(models.Model):
    pro_name = models.CharField(max_length=32)
    pro_description = models.TextField()
    pro_image = models.TextField()
    pro_code = models.CharField(max_length=32, primary_key=True)
    pro_range = models.CharField(max_length=32)
    pro_features = models.TextField(default="")
    pro_price = models.IntegerField()
    pro_price_per_user = models.IntegerField()
    pro_price_plumber = models.IntegerField()
    pro_price_prime = models.IntegerField()


    
