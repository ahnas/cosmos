from django.contrib import admin
from .models import CycleService,ShuttleService,FitnessServiceOnsite,FitnessServiceBranch

# Register your models here.

admin.site.register(CycleService)
admin.site.register(ShuttleService)
admin.site.register(FitnessServiceBranch)
admin.site.register(FitnessServiceOnsite)