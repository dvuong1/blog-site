from django.shortcuts import render
from django.views.generic import ListView, DetailView
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