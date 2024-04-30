from django.shortcuts import render
from Blog.models import Post, CategoryPost


# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {"posts": posts})


def category(request, category_id):
    cat = CategoryPost.objects.get(id=category_id)
    posts = Post.objects.filter(category=cat)
    return render(request, 'category.html', {"posts": posts, "category": cat})
