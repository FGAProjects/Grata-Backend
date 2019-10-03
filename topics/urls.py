from django.urls import path

from topics.api.views import TopicsListView

urlpatterns = [
    path('', TopicsListView.as_view()),
]