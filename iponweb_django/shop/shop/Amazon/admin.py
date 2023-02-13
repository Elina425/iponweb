from django.contrib import admin
from .models import Customer
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    list_display = ("id", "registrated_at", "user_info")
    def user_info(self, obj):
        if obj.user:
            return "{}".format(" ". join(list(obj.user.first_name, obj.user.last_name)))
admin.site.register(Customer, BuyerAdmin)