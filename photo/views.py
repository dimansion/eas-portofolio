from django.shortcuts import render
from .models import Work

def post_list(request):
    posts = Work.objects.all()
    return render(request, 'photo/index.html', {'posts': posts})


