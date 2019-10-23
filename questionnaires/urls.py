from django.urls import path

from questionnaires.api.views import QuizListView

urlpatterns = [
    path('', QuizListView.as_view()),
]