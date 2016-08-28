from django.shortcuts import render
from .models import Work
from .forms import WorkForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Work.objects.all()
    return render(request, 'photo/post_list.html', {'posts': posts})

@login_required
def post_new(request):
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = request.FILES['image']
            post.save()
            return redirect('post_list')
    else:
        form = WorkForm()
    return render(request, 'photo/post_edit.html', {'form': form})
