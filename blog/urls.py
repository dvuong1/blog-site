from django.urls import path
from .views import MsgListView, MsgDetailView
from . import views

urlpatterns = [
    path('', MsgListView.as_view(), name='blog-home'),
    path('message/<int:pk>/', MsgDetailView.as_view(), name='message-detail'),
    path('about/', views.about, name='blog-about'),
]
