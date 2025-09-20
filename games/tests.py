from rest_framework.test import APITestCase
from rest_framework import status
from .models import Game, Review

class GameAPITest(APITestCase):

    def setUp(self):
        self.game1 = Game.objects.create(title="Half-Life", genre="Shooter")
        self.game2 = Game.objects.create(title="Doom", genre="Shooter")

    def test_get_games_list(self):
        response = self.client.get("/api/games/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_game(self):
        data = {"title": "Portal", "genre": "Puzzle"}
        response = self.client.post("/api/games/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.count(), 3)

    def test_filter_games_by_genre(self):
        response = self.client.get("/api/games/?genre=Shooter")
        self.assertEqual(len(response.data), 2)

    def test_invalid_rating(self):
        data = {"game": self.game1.id, "text": "Bad game", "rating": 25}
        response = self.client.post("/api/reviews/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReviewAPITest(APITestCase):
    def setUp(self):
        self.game = Game.objects.create(title="Half-Life", genre="Shooter")
        # Создаём несколько отзывов для тестов фильтров и поиска
        self.review1 = Review.objects.create(game=self.game, text="Отличная игра", rating=10)
        self.review2 = Review.objects.create(game=self.game, text="Не очень", rating=5)

    def test_create_review(self):
        data = {"game": self.game.id, "text": "Классно!", "rating": 8}
        response = self.client.post("/api/reviews/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 3)

    def test_invalid_rating(self):
        data = {"game": self.game.id, "text": "Плохая игра", "rating": 25}
        response = self.client.post("/api/reviews/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_reviews_by_rating(self):
        response = self.client.get("/api/reviews/?rating=10")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['text'], "Отличная игра")

    def test_search_reviews_by_text(self):
        response = self.client.get("/api/reviews/?search=Не")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['text'], "Не очень")
