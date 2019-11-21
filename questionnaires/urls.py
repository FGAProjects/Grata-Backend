from django.urls import path

from questionnaires.api.views import QuizListView, QuizCreateView, QuizMeetingListView

urlpatterns = [

    path('', QuizListView.as_view()),
    path('create/', QuizCreateView.as_view()),
    path('questtionaire_meeting/<pk>', QuizMeetingListView.as_view())
]