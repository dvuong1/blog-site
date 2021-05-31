from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView
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

class MsgDetailView(DetailView):
    model = Message

class MsgCreateView(CreateView):
    model = Message
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)