from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.SET_NULL)
    device_id = models.CharField(max_length = 200, null = True, blank = True)
    profile_picture = models.ImageField(null=True)
    first_name = models.CharField(max_length = 250, null = True)
    last_name = models.CharField(max_length = 250, null = True)
    email = models.EmailField(max_length = 250, null = True, blank = True)
    address_line_1 = models.CharField(max_length = 250, null = True)
    address_line_2 = models.CharField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length = 250, null = True)
    state = models.CharField(max_length = 250, null = True)
    country = models.CharField(max_length = 250, default = "Nigeria")
    postal_code = models.PositiveIntegerField(null = True)
    phone_number = models.PositiveIntegerField(null = True)
    slug = AutoSlugField(populate_from='__str__')

    def __str__(self):
    	if self.user:
    		name = self.user.username
    	else:
    		name = self.device_id
    	return str(name)

class DeliveryAddress(models.model):
    customer = models.ForeignKey(customer)
    first_name = models.CharField(max_length = 250, null = True)
    last_name = models.CharField(max_length = 250, null = True)
    email = models.EmailField(max_length = 250, null = True, blank = True)
    address_line_1 = models.CharField(max_length = 250, null = True)
    address_line_2 = models.CharField(max_length = 250, null = True, blank = True)
    city = models.CharField(max_length = 250, null = True)
    state = models.CharField(max_length = 250, null = True)
    country = models.CharField(max_length = 250, default = "Nigeria")
    postal_code = models.PositiveIntegerField(null = True)
    phone_number = models.PositiveIntegerField(null = True)

class DefaultAddress(models.model):
    customer = models.ForeignKey(customer)
    DeliveryAddress = models.ForeignKey(DeliveryAddress)