from django.contrib import admin
from .models import Customer
from .models import Category
from .models import Item
from .models import Store
from .models import StoreOwner
from .models import Mybug
from .models import Purchase
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "registrated_at", "user_info")
    def user_info(self, obj):
        if obj.user:
            return "{}".format(" ". join(list(obj.user.first_name, obj.user.last_name)))
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'created_by', 'image', 'price', 'quantity', 'info', 'store']
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'store_category']
@admin.register(StoreOwner)
class StoreOwnerAdmin(admin.ModelAdmin):
    horizontal_filter = ['name', 'avatar', 'registered_at', 'slug']
@admin.register(Mybug)
class MybugAdmin(admin.ModelAdmin):
    horizontal_filter = ['items', 'customer', 'total_price']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    horizontal_filter = ['items', 'buy_time', 'customer', 'total_price']

admin.site.register(Customer, CustomerAdmin)