from django.contrib import admin

# Register your models here.

from .models import Product
from .models import Contact
from .models import Orders

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
