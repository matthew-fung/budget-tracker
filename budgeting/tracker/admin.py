from django.contrib import admin

# Register your models here
from .models import Expenses, Revenues

admin.site.register(Expenses)
admin.site.register(Revenues)
