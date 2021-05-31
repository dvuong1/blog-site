from django.urls import path
from .views import (
    MsgListView, MsgDetailView, MsgCreateView, MsgUpdateView
)
from . import views

urlpatterns = [
    path('', MsgListView.as_view(), name='blog-home'),
    path('message/<int:pk>/', MsgDetailView.as_view(), name='message-detail'),
    path('message/new/', MsgCreateView.as_view(), name='message-create'),
    path('message/<int:pk>/update/', MsgUpdateView.as_view(), name='message-update'),
    path('about/', views.about, name='blog-about'),
]
