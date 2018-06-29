from django.contrib import admin

from .models import Country
from .models import Profile

# Register your models here.
admin.site.register(Country)
admin.site.register(Profile)
