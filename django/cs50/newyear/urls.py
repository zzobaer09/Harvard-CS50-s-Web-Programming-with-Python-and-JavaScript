from django.urls import path
from . import views

urlpatterns = [
    path("", views.isNewYear , name="new year"),
    path("now" , views.NowDate , name="now date")
]