from django.urls import path
from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index_profile, name="index_profile"),
    path("category/<str:pk>/", views.categories, name="categories"),
    path("add_card", views.add_card, name="add_card"),
]
