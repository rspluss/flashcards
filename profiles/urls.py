from django.urls import path
from profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index_profile, name="index_profile"),
]
