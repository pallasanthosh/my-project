from django.contrib import admin

# Register your models here.

from .models import Feature
from .models import Employee
# Register your models here.
admin.site.register(Feature)
admin.site.register(Employee)
