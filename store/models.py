from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    is_subscriber = models.BooleanField(default=False)  # New field

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.first_name}{self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100 ,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=4000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    file = models.FileField(upload_to='uploads/pdfs',null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    
 
    def __str__(self):
        return self.name
