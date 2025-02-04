from django.urls import path
from foods.views import FoodCategoryListAPIView


urlpatterns = [
    path("foods/", FoodCategoryListAPIView.as_view(), name='food_list'),
]
