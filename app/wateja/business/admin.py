from django.contrib import admin
from .models import Category, Business


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Category, CategoryAdmin)


# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]


admin.site.register(Business, BusinessAdmin)
