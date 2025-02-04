from django.http import JsonResponse
from rest_framework.views import APIView
from .models import FoodCategory, Food


class FoodCategoryListAPIView(APIView):
    def get(self, request):
        # Получаем все категории
        categories = FoodCategory.objects.all()
        data = []

        for category in categories:
            # Фильтруем блюда по is_publish
            published_foods = category.food.filter(is_publish=True)

            # В выборку попадают только те категории, у которых есть хотя бы 1 опубликованный товар
            if len(published_foods) != 0:

                # Формируем список блюд для текущей категории
                foods_data = []
                for food in published_foods:
                    foods_data.append({
                        'id': food.id,
                        'name_ru': food.name_ru,
                        'description_ru': food.description_ru,
                        'cost': float(food.cost),  # DecimalField конвертируем в float для JSON
                        'is_vegan': food.is_vegan,
                        'is_special': food.is_special,
                    })

                # Формируем данные для категории
                category_data = {
                    'id': category.id,
                    'name_ru': category.name_ru,
                    'name_en': category.name_en,
                    'name_ch': category.name_ch,
                    'order_id': category.order_id,
                    'foods': foods_data,
                }
                data.append(category_data)

        return JsonResponse(data, safe=False)