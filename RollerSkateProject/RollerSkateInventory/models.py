from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RollerSkate(models.Model):
    name = models.CharField(max_length=20, blank=True)
    size = models.IntegerField(choices= [
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
        (32, '32'),
        (33, '33'),
        (34, '34'),
    ], blank=True)
    barcode = models.IntegerField(blank=True)
    inventory = models.ForeignKey(Inventory, related_name='rollerskates', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name