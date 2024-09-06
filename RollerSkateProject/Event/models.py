from django.db import models
from django.utils import timezone
from Inventory.models import Inventory, RollerSkate

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    inventories = models.ManyToManyField(Inventory)
    last_updated = models.DateTimeField(auto_now=True)

class Order(models.Model):
    rollerskates = models.ManyToManyField(RollerSkate, related_name='orders')
    event = models.ForeignKey(Event, related_name='orders', on_delete=models.DO_NOTHING)
    borrow_at = models.DateTimeField(default=timezone.now)
    retrieved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'Order {self.id} by {self.client}'

class Client(models.Model):
    STATUS_CHOICE = [(0, "alone"), (1,"parent"), (2,"child")]
    status = models.TextField(choices=STATUS_CHOICE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    order = models.ForeignKey(Order, related_name="clients", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'