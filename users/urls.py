from django.urls import path
from users.api.views import UserList, UserDetail, UserUpdate, DeleteUser

urlpatterns = [
    path('usuarios', UserList.as_view()),
    path('detalhes/<int:pk>/', UserDetail.as_view()),
    path('alterar_informacoes/<int:pk>/', UserUpdate.as_view()),
    path('excluir_usuario/<int:pk>/', DeleteUser.as_view())
]