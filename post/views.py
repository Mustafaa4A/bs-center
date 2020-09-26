from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-date')
    for post in posts:
        if len(post.body) > 330:
            post.body = post.body[:330]+'....'

    return render(request, 'index.html', {'posts': posts})


def new_post(request):
    if request.method == 'POST':
        post = Post(request.POST, request.FILES)
        title = request.POST['title']
        body = request.POST['body']
        author = request.POST['author']
        img = request.FILES['img']
        post = Post.objects.create(
            title=title, body=body, img=img, author=author)
        post.save()
        return redirect('/')
    else:
        return render(request, 'new_post.html')


def about(request):
    return render(request, 'about.html')


def post_detail(request, pk):
    if request.method == 'POST':
        user = request.POST['user']
        body = request.POST['comment']
        post = Post.objects.get(pk=pk)
        comment = Comment.objects.create(user=user, body=body, post=post)
        comment.save()
        return redirect('/')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
