from django.contrib import admin
from flashcard.models import Category, FlashCard, Card

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    list_filter = ["name"]


@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ["id", "name_pl", "name_eng", "category"]
    list_filter = ["name_pl", "name_eng", "category"]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["id", "question", 'answer', "box"]
