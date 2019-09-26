from django.urls import path

from topics.api.views import TopicsListView, TopicCreateView, TopicDeleteView

urlpatterns = [
    path('', TopicsListView.as_view()),
    path('create/', TopicCreateView.as_view()),
    path('delete/<pk>/', TopicDeleteView.as_view())
]