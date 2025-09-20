from rest_framework import serializers
from .models import Game, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        """Проверка, что рейтинг от 0 до 10"""
        if not 0 <= value <= 10:
            raise serializers.ValidationError("Рейтинг должен быть от 0 до 10")
        return value

class GameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = '__all__'

    def validate(self, attrs):
        """Проверка, что обязательные поля заполнены"""
        if not attrs.get("title"):
            raise serializers.ValidationError({"title": "Название игры обязательно"})
        if not attrs.get("genre"):
            raise serializers.ValidationError({"genre": "Жанр обязателен"})
        return attrs