from django.contrib import admin
from django.urls import path
from .views import LoginView, RegisterView, RefreshView, GetSecuredData, OrganizeQuizView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path("getdata/", GetSecuredData.as_view()),
    path("organize_quiz/", OrganizeQuizView.as_view())
]
