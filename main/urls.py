from django.urls import path
from . import views


urlpatterns = [
    path('', views.HelloView.as_view()),
    path('index/', views.IndexWebSocket.as_view())
]
