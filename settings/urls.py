from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('sectors/', include('sectors.urls')),
    path('meetings/', include('meetings.urls')),
    path('topics/', include('topics.urls')),
    path('rules/', include('rules.urls')),
    path('questionnaires/', include('questionnaires.urls')),
    path('choices/', include('choices.urls')),
    path('answers/', include('answers.urls'))
]