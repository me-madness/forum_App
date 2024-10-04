from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from forumApp.posts.forms import PersonForm


def index(request):

    form = PersonForm(request.POST or None)

    context = {
        "my_form": form,
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "Django project?",
                "author": "Rangel Petrov",
                "content": "How to create a Django project",
                "created_at": datetime.now(),
            },
            {
                "title": "React project?",
                "author": "Boris Petrov",
                "content": "How to create a React project",
                "created_at": datetime.now(),
            },
            {
                "title": "Angular project?",
                "author": "Samuil Petrov",
                "content": "How to create a Angular project",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)
