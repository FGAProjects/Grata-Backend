from django.urls import path

from questionnaires.api.views import QuesttionaireCreateView, QuesttionaireDetailView, \
                                     QuesttionaireListView, QuesttionaireMeetingView, QuizListView, \
                                     QuizDetailView, QuizMeetingListView

urlpatterns = [

    path('', QuesttionaireListView.as_view()),
    path('create/', QuesttionaireCreateView.as_view()),
    path('detail/<pk>/', QuesttionaireDetailView.as_view()),
    path('questtionaires_meeting/<pk>/', QuesttionaireMeetingView.as_view()),
    path('quiz_list/', QuizListView.as_view()),
    path('quiz_detail/<pk>/', QuizDetailView.as_view()),
    path('quiz_meeting/<pk>/', QuizMeetingListView.as_view())
]