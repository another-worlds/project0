from django.contrib import admin
from .models import MyModel, MySubmodel

# Register your models here.
admin.site.register(MyModel)
admin.site.register(MySubmodel)