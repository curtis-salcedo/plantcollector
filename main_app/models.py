from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

# FERTILIZERS = (
#     ('G', 'General'),
#     ('N', 'High Nitrogen'),
#     ('P', 'High Phosphorous'),
#     ('K', 'High Potassium'),
#     ('W', 'Worm Castings'),
#     ('S', 'Seaweed Extract'),
# )

class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField()
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.type
    
    def get_absolute_url(self):
        return reverse('fertilizers_detail', kwargs={'pk': self.id})

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    fertilizers = models.ManyToManyField(Fertilizer)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
    def water_check(self):
        return self.watering_set.filter(water=True).order_by('-date').first()
    
class Watering(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    water = models.BooleanField(default=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"On {self.date}, the {self.plant} plant was watered "
        
    class Meta:
        ordering = ['-date']