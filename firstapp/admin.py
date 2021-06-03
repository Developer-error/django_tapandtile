from django.contrib import admin
from .models import Slider,Option, SmallOption, Product

# Register your models here.

admin.site.register(Slider)
admin.site.register(Option)
admin.site.register(SmallOption)
admin.site.register(Product)