from django.http import JsonResponse
from rest_framework.views import APIView
from .models import FoodCategory, Food
from .services import get_response_data


class FoodCategoryListAPIView(APIView):

    def get(self, request):
        # Получаем все категории
        categories = FoodCategory.objects.all()

        data = get_response_data(categories=categories)

        return JsonResponse(data, safe=False)