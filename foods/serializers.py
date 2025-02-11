from rest_framework import serializers
from foods.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')


#  РАСШИРИМ СЕРИАЛИЗАТОР МЕТОДОМ get_food(self, obj) для фильтрации блюд
class FoodListSerializer(serializers.ModelSerializer):
    foods = serializers.SerializerMethodField()

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')

    def get_foods(self, obj):
        # Фильтрация связанных Food, чтобы оставить только те, у которых is_publish=True
        foods = obj.food.filter(is_publish=True)
        print(foods)
        return FoodSerializer(foods, many=True, read_only=True).data
