from django.contrib import admin
from flashcard.models import Category, FlashCard

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_filter = ["name"]


@admin.register(FlashCard)
class FlashCardAdmin(admin.ModelAdmin):
    list_display = ["name_pl", "name_eng", "category"]
    list_filter = ["name_pl", "name_eng", "category"]
