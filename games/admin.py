from django.contrib import admin
from .models import Game, Review

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date')
    search_fields = ('title', 'genre')
    list_filter = ('genre',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'text', 'rating')
    search_fields = ('text',)
    list_filter = ('game',)

