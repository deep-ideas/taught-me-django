from django.contrib import admin

# Register your models here.
from .models import OneTimePayment

admin.site.register(OneTimePayment)