from django.db import models
from django.urls import reverse
from datetime import date

# TIMES = (
#     ('M', 'Morning'),
#     ('A', 'Afternoon'),
#     ('E', 'Evening')
# )

# FERTILIZERS = (
#     ('G', 'General'),
#     ('N', 'High Nitrogen'),
#     ('P', 'High Phosphorous'),
#     ('K', 'High Potassium'),
#     ('W', 'Worm Castings'),
#     ('S', 'Seaweed Extract'),
# )

# class Fertilizer(models.Model):
#     name = models.CharField(max_length=50)
#     type = models.CharField()
#     description = models.TextField(max_length=1024)

#     def __str__(self):
#         return self.type
    
#     def get_absolute_url(self):
#         return reverse('fertilizers_detail', kwargs={'pk': self.id})

# # Create your models here.
# class Plant(models.Model):
#     name = models.CharField(max_length=25)
#     type = models.CharField(max_length=25)
#     description = models.TextField(max_length=250)
#     fertilizers = models.ManyToManyField(Fertilizer)

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'plant_id': self.id})
    
#     def water_check(self):
#         return self.watering_set.filter(water=True).order_by('-date').first()
    
# class Watering(models.Model):
#     date = models.DateField()
#     time = models.CharField(
#         max_length=1,
#         choices=TIMES,
#         default=TIMES[0][0]
#     )
#     water = models.BooleanField(default=True)
#     plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"On {self.date}, the {self.plant} plant was watered "
        
#     class Meta:
#         ordering = ['-date']

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    # profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    location = models.CharField(max_length=255)
    garden_size = models.IntegerField(null=True, blank=True)

class Plant(models.Model):
    TYPE_CHOICES = [
        ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
        ('herb', 'Herb'),
        ('flower', 'Flower'),
    ]

    LIFE_CYCLE_CHOICES = [
        ('annual', 'Annual'),
        ('perennial', 'Perennial'),
        ('biennial', 'Biennial'),
    ]

    WATERING_REQUIREMENTS_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=255)
    variety = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    life_cycle = models.CharField(max_length=255, choices=LIFE_CYCLE_CHOICES, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # image = models.ImageField(upload_to='plant_images', null=True, blank=True)
    edible = models.BooleanField(default=False)
    companion_plants = models.ManyToManyField('self', symmetrical=False, blank=True)
    pests = models.TextField(null=True, blank=True)
    diseases = models.TextField(null=True, blank=True)
    watering_requirements = models.CharField(max_length=255, choices=WATERING_REQUIREMENTS_CHOICES, null=True, blank=True)
    spacing_x_min = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    spacing_x_max = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    spacing_y_min = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    spacing_y_max = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

class GrowingEnvironment(models.Model):
    SUN_EXPOSURE_CHOICES = [
        ('full_sun', 'Full Sun'),
        ('partial_sun', 'Partial Sun'),
        ('partial_shade', 'Partial Shade'),
        ('full_shade', 'Full Shade'),
    ]
    name = models.CharField(max_length=255)
    water_requirements = models.CharField(max_length=255)
    sun_exposure = models.CharField(max_length=255, choices=SUN_EXPOSURE_CHOICES, null=True, blank=True)
    temperature_range = models.CharField(max_length=255, null=True, blank=True)
    light_requirements = models.CharField(max_length=255, null=True, blank=True)
    soil_type = models.CharField(max_length=255, null=True, blank=True)

class Fertilizer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    organic = models.BooleanField(default=False)
    nitrogen = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    phosphorus = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    potassium = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

class Garden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class UserPlant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    environment = models.ForeignKey(GrowingEnvironment, on_delete=models.CASCADE)
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE, related_name='plants')
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.SET_NULL, null=True, blank=True)
    planting_date = models.DateField(null=True, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    progress = models.CharField(max_length=255, null=True, blank=True)
    yield_production = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    success = models.BooleanField(default=False)
    failure_reason = models.TextField(null=True, blank=True)