from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.SET_NULL)
    device_id = models.CharField(max_length = 200, null = True, blank = True)
    profile_picture = models.ImageField(null=True)
    address = models.TextField(null=True)
    phone_number = models.PositiveIntegerField(null=True)
    slug = AutoSlugField(populate_from='__str__')

    def __str__(self):
    	if self.user:
    		name = self.user.username
    	else:
    		name = self.device_id
    	return str(name)
