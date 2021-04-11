from django.urls import path, include
from . import views

app_name = "members"

urlpatterns = [
    path('', views.UserView.as_view()),
    path('login/', views.login),
]
