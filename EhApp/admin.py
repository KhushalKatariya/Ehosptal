from django.contrib import admin
from .models import *

# Register your models here.
class SuperAdmin(admin.ModelAdmin):
    admin.site.site_header = admin.site.site_title = 'Ehospital App'
    
all_models = (Master, Profile, Department, Appointment,)

for model in all_models:
    admin.site.register(model, SuperAdmin)

# admin.site.register(Master)
# admin.site.register(Profile)
# admin.site.register(Department)