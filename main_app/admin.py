from django.contrib import admin
from .models import User, Plant, GrowingEnvironment, Fertilizer, Garden, UserPlant

# Admin Site Header
admin.site.site_header = "Garden Planner Admin"

# Admin Classes
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')


# Models Registered Below
admin.site.register(User)
admin.site.register(Plant)
admin.site.register(GrowingEnvironment)
admin.site.register(Fertilizer)
admin.site.register(Garden)
admin.site.register(UserPlant)
