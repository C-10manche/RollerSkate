from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class RollerSkate(models.Model):
    name = models.CharField(max_length=50)
    SIZE_CHOICES = [(i, str(i)) for i in range(28, 46)]
    size_min = models.IntegerField(choices=SIZE_CHOICES)
    size_max = models.IntegerField(choices=SIZE_CHOICES, null=True, blank=True)
    barcode = models.IntegerField()
    inventory = models.ForeignKey(Inventory, related_name='rollerskates', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.size_max:
            if self.size_min:
                self.size_max = self.size_min
        elif self.size_min>self.size_max:
            saved_size_max = self.size_max
            self.size_max = self.size_min
            self.size_min = saved_size_max        
        super(RollerSkate, self).save(*args, **kwargs)

class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    inventories = models.ManyToManyField(Inventory)
    
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default='youremail@email.com', unique=True, max_length=254)
    
    AGE_CHOICES = [(age, str(age)) for age in range(121)]
        
    age = models.IntegerField(choices=AGE_CHOICES, null=True, blank=True)

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    parents = models.ManyToManyField(Client, related_name="childrens")
    
class Order(models.Model):
    clients = models.ManyToManyField(Client, related_name="orders")
    rollerskates = models.ManyToManyField(RollerSkate, related_name='orders')
    event = models.ManyToManyField(Event, related_name='orders')
    borrow_at = models.DateTimeField(default=timezone.now)
    retrieved_at = models.DateTimeField(null=True, blank=True)
    
    