from django.urls import path

from gradedquesttionaire.api.views import GradedQuesttionaireListView, GradedQuesttionaireQuizView, \
                                          GradedQuesttionaireCreateView

urlpatterns = [

    path('', GradedQuesttionaireListView.as_view()),
    path('detail/<pk>/', GradedQuesttionaireQuizView.as_view()),
    path('create/', GradedQuesttionaireCreateView.as_view())
]