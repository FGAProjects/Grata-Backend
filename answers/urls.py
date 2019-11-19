from django.urls import path

from answers.api.views import AnswerListView

urlpatterns = [
    path('', AnswerListView.as_view()),
]