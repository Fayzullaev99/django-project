from django.contrib import admin

from shop.models import *

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Offer)
admin.site.register(Vendor)
