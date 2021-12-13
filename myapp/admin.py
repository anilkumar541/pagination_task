from django.contrib import admin

# Register your models here.
from myapp.models import Quote, Category


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display =["id", "text", "created_at", "updated_at"]


    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =["id", "category", "created_at", "updated_at"]