from django.urls import path

from setors.api.views import SetorListView, SetorCreateView, \
                               SetorDetailView, SetorUpdateView, SetorDeleteView

urlpatterns = [
    path('', SetorListView.as_view()),
    path('create/', SetorCreateView.as_view()),
    path('detail/<pk>', SetorDetailView.as_view()),
    path('update/<pk>', SetorUpdateView.as_view()),
    path('delete/<pk>', SetorDeleteView.as_view())
]