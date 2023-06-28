from django.contrib import admin
from .models import Cat, Dog, Owner


# Register your models here.
admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(Owner)