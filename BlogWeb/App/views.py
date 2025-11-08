from django.shortcuts import render, redirect
from .models import *
from .forms import CommentForm
# Create your views here.
def blog(request):
    posts = Blog.objects.all()
    carsoul = Blog.objects.all().order_by('-id')[:4]

    search_value = request.GET.get('search') or ""
    if search_value:
        posts = Blog.objects.filter(title__icontains=search_value)

    context={
        'post': posts,
        'carsoul':carsoul,
        'search_value': search_value
          }
    return render(request, 'list.html',context)
    


def blog_detail(request,pk):
    post = Blog.objects.get(id=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'details.html', context={'post':post, 'forms':form, 'comments':comments})

def postLike(request,pk):
    post = Blog.objects.get(id=pk)
    post.like +=1
    post.save()
    return redirect('detail', pk=pk)
