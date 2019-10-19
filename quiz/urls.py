from django.urls import path

from quiz.api.views import QuizListView

urlpatterns = [
    path('', QuizListView.as_view()),
]