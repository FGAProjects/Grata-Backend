from django.urls import path

from topics.api.views import TopicsListView, TopicCreateView, TopicDeleteView, TopicsList

urlpatterns = [
    path('', TopicsList.as_view()),
    path('create/', TopicCreateView.as_view()),
    path('topics_in_meeting/<pk>/', TopicsListView.as_view()),
    path('delete/<pk>/', TopicDeleteView.as_view())
]