from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Game, Review
from .serializers import GameSerializer, ReviewSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre']
    search_fields = ['title']
    ordering_fields = ['title', 'id']
    ordering = ['id']

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['rating']
    search_fields = ['text']