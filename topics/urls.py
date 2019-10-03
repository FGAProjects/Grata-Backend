from django.urls import path

from topics.api.views import TopicsList

urlpatterns = [
    path('', TopicsList.as_view()),
]