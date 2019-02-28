from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    # path("congrats/", views.congrats, name="congrats"),
]