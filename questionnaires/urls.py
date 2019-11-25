from django.urls import path

from questionnaires.api.views import QuesttionaireCreateView, QuesttionaireDetailView, \
                                     QuesttionaireListView, QuesttionaireMeetingView

urlpatterns = [

    path('', QuesttionaireListView.as_view()),
    path('create/', QuesttionaireCreateView.as_view()),
    path('detail/<pk>/', QuesttionaireDetailView.as_view()),
    path('questtionaires_meeting/<pk>/', QuesttionaireMeetingView.as_view())
]