from django.contrib import admin
from shop.models import *

class ProductSizeGather(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductImageGather(admin.TabularInline):
    model = Gallery
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price","quantity","color"]
    list_display_links = ["title","color"]
    list_editable = ["quantity"]
    list_filter = ["price"]
    inlines = [ProductSizeGather, ProductImageGather]


admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Offer)
admin.site.register(Vendor)
