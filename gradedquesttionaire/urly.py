from django.urls import path

from gradedquesttionaire.api.views import GradedQuesttionaireListView, GradedQuesttionaireQuizView

urlpatterns = [

    path('', GradedQuesttionaireListView.as_view()),
    path('detail/<pk>/', GradedQuesttionaireQuizView.as_view())
]