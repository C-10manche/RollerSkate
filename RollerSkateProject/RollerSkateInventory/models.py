from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RollerSkate(models.Model):
    name = models.CharField(max_length=20)
    modulable = models.BooleanField(default=False)
    SIZE_CHOICES = [
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
        (32, '32'),
        (33, '33'),
        (34, '34'),
        (35, '35'),
        (36, '36'),
        (37, '37'),
        (38, '38'),
        (39, '39'),
        (40, '40'),
        (41, '41'),
        (42, '42'),
        (43, '43'),
        (44, '44'),
        (45, '45'),
    ]
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
            size = self.size_max
            self.size_max = self.size_min
            self.size_min = self.size_max
        super(RollerSkate, self).save(*args, **kwargs)
    
