from django.shortcuts import render
from .models import Messages

posts = [
    {
        'author': 'Dan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'author': 'Tan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 29, 2020'
    },
]

def home(request):
    context = {
        'messages': Messages.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About',
    })