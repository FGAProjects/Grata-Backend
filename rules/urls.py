from django.urls import path

from rules.api.views import RulesListView

urlpatterns = [
    path('', RulesListView.as_view()),
]