from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Message

def home(request):
    context = {
        'message_set': Message.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About',
    })

class MsgListView(ListView):
    model = Message
    template_name = 'blog/home.html'
    context_object_name = 'message_set'
    ordering = ['-date_posted']
    paginate_by = 5

class UserMsgListView(ListView):
    model = Message
    template_name = 'blog/user_messages.html'
    context_object_name = 'message_set'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Message.objects.filter(author=user).order_by('-date_posted')


class MsgDetailView(DetailView):
    model = Message

class MsgCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MsgUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        message = self.get_object()
        if self.request.user == message.author:
            return True
        return False

class MsgDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = '/'

    def test_func(self):
        message = self.get_object()
        if self.request.user == message.author:
            return True
        return False