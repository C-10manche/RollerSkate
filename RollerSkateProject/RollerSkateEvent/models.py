from django.db import models
from django.utils import timezone
from RollerSkateInventory.models import Inventory, RollerSkate

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    inventories = models.ManyToManyField(Inventory)
    
from django.db import models

class Client(models.Model):
    STATUS_CHOICE = [(0, "alone"), (1,"parent"), (2,"child")]
    status = models.TextField(choices=STATUS_CHOICE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Order(models.Model):
    client = models.ManyToManyField(Client, related_name="orders")
    rollerskates = models.ManyToManyField(RollerSkate, related_name='orders')
    event = models.ForeignKey(Event, related_name='orders', on_delete=models.CASCADE)
    borrow_at = models.DateTimeField(default=timezone.now)
    retrieved_at = models.DateTimeField(null=True, blank=True)
    