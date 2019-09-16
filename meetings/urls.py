from django.urls import path

from meetings.api.views import MeetingListView, MeetingCreateView

urlpatterns = [
    path('', MeetingListView.as_view()),
    path('create/', MeetingCreateView.as_view()),
    # path('detail/<pk>/', ProjectDetailView.as_view()),
    # path('update/<pk>/', ProjectUpdateView.as_view()),
    # path('delete/<pk>/', ProjectDeleteView.as_view())
]