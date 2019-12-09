from django.urls import path

from comments.api.views import CommentCreateView, CommentListView, CommentDeleteView, CommentQuesttionaireView

urlpatterns = [

    path('', CommentListView.as_view()),
    path('detail/<pk>/', CommentQuesttionaireView.as_view()),
    path('create/', CommentCreateView.as_view()),
    path('delete/<pk>/', CommentDeleteView.as_view()),
]