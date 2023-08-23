from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.HelloView.as_view()),
    path('', views.IndexWebSocket.as_view())
]
