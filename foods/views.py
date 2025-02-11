from rest_framework.generics import ListAPIView
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListAPIView(ListAPIView):
    """Вывод списка категорий"""

    # В Queryset попадут только те категории, у которых есть опубликованные блюда, но с дубликатами.
    queryset = FoodCategory.objects.filter(food__is_publish=True)
    serializer_class = FoodListSerializer

    def get_queryset(self):
        """Форматируем Queryset"""

        queryset = super().get_queryset()

        # Уберем дубли из набора данных:
        new_query = []
        for category in queryset:
            if category not in new_query:
                new_query.append(category)

        return new_query

