from django.db.models import Q, Count
from rest_framework.generics import ListAPIView
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListAPIView(ListAPIView):
    """Вывод списка категорий"""

    serializer_class = FoodListSerializer

    def get_queryset(self):
        """Получение Queryset"""
        # Возвращает множества объектов с is_publish = True
        food_count = Count('food', filter=Q(food__is_publish=True))
        # Использование аннотации для получения категорий в которых есть хотя бы одно опубликованное блюдо
        queryset = FoodCategory.objects.annotate(food_count=food_count).filter(food_count__gt=0)

        return queryset


