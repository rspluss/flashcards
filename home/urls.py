from django.urls import path
from home import views

app_name = "flashcards"

urlpatterns = [
    path("", views.index, name="home"),
    path("shop/", views.shop, name="shop"),
    path("price/", views.price, name="price"),
]
