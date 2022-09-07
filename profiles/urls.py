from django.urls import path
from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index_profile, name="index_profile"),
    path("category/<str:pk>/", views.categories, name="categories"),
    path("add_card", views.add_card, name="add_card"),
    path("register_user/", views.register_user, name="register_user"),
    path("edit", views.edit_profile, name="edit"),
    path("edit/<str:pk>/", views.edit_card, name="edit_card"),
    path("box/<str:box_num>/", views.BoxView.as_view(), name="box"),
]
