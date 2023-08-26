from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.HelloView.as_view()),
    path('', views.IndexWebSocket.as_view()),
    path('chat/<str:username>/', views.JoinChat.as_view()),
    path('chat/new/<str:username>/', views.NewMessage.as_view())
]
