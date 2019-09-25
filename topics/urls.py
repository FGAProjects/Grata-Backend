from django.urls import path

from topics.api.views import TopicsListView, TopicCreateView, TopicDetailView, TopicDeleteView

urlpatterns = [
    path('', TopicsListView.as_view()),
    path('create/', TopicCreateView.as_view()),
    path('detail/int<pk>/', TopicDetailView.as_view()),
    path('delete/int<pk>/', TopicDeleteView.as_view())
]