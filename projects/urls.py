from django.urls import path

from projects.api.views import ProjectListView, ProjectCreateView, \
                               ProjectDetailView, ProjectUpdateView, \
                               ProjectDeleteView, ProjectsSectorsListView

urlpatterns = [
    path('', ProjectListView.as_view()),
    path('create/', ProjectCreateView.as_view()),
    path('detail/<pk>/', ProjectDetailView.as_view()),
    path('update/<pk>/', ProjectUpdateView.as_view()),
    path('delete/<pk>/', ProjectDeleteView.as_view()),
    path('list_projects_sectors/', ProjectsSectorsListView.as_view())
]