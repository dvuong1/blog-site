from django.urls import path
from .views import (
    MsgListView, MsgDetailView, MsgCreateView, MsgUpdateView, MsgDeleteView, UserMsgListView
)
from . import views

urlpatterns = [
    path('', MsgListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserMsgListView.as_view(), name='user-messages'),
    path('message/<int:pk>/', MsgDetailView.as_view(), name='message-detail'),
    path('message/new/', MsgCreateView.as_view(), name='message-create'),
    path('message/<int:pk>/update/', MsgUpdateView.as_view(), name='message-update'),
    path('message/<int:pk>/delete/', MsgDeleteView.as_view(), name='message-delete'),
    path('about/', views.about, name='blog-about'),
]
