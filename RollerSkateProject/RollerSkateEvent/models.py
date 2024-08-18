from django.db import models
from django.utils import timezone
from RollerSkateInventory.models import Inventory, RollerSkate

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    inventories = models.ManyToManyField(Inventory)
    
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254, null=True, blank=True)
    
    AGE_CHOICES = [(age, str(age)) for age in range(121)]
        
    age = models.IntegerField(choices=AGE_CHOICES, null=True, blank=True)
    
class Order(models.Model):
    clients = models.ManyToManyField(Client, related_name="orders")
    rollerskates = models.ManyToManyField(RollerSkate, related_name='orders')
    event = models.ManyToManyField(Event, related_name='orders')
    borrow_at = models.DateTimeField(default=timezone.now)
    retrieved_at = models.DateTimeField(null=True, blank=True)
    