from django.contrib import admin
from .models import Cake,AddCaketoCart,Checkout
# Register your models here.


admin.site.register(Cake)
admin.site.register(AddCaketoCart)
admin.site.register(Checkout)
