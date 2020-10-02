from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ('title','size','purpose','type')
    search_fields = ('title','size','purpose','type','bedrooms','bathroom')

    filter_horizontal = ()
    list_filter = ('bedrooms','bathroom','city','size')
    fieldsets = ()


admin.site.register(SellerProperty,SellerAdmin)

class ApproveAdmin(admin.ModelAdmin):
    fields = ('approval','request_approval')
    list_display = ('seller_title','request_approval')
admin.site.register(Approve,ApproveAdmin)