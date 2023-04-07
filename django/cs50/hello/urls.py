from django.urls import path
from . import views

urlpatterns = [
    path("" , views.hello , name="just hello"),
    path("zobaer" , views.helloZo , name="zobaer"),
    path("<str:name>", views.greet , name="greed"),
]