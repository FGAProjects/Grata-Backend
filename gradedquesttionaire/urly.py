from django.urls import path

from gradedquesttionaire.api.views import GradedQuesttionaireListView, GradedQuesttionaireQuizView, \
                                          GradedQuesttionaireCreateView, GradedQuesttionaireInQuesttionaireListView, \
                                          GradedQuesttionaireDelete

urlpatterns = [

    path('', GradedQuesttionaireListView.as_view()),
    path('detail/<pk>/', GradedQuesttionaireQuizView.as_view()),
    path('create/', GradedQuesttionaireCreateView.as_view()),
    path('delete/<pk>/', GradedQuesttionaireDelete.as_view()),
    path('list_in_questtionaire/<pk>/', GradedQuesttionaireInQuesttionaireListView.as_view()),
]