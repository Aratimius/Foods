from django.contrib import admin

from foods.models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name_ru', 'category')


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name_ru')
