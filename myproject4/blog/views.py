from django.shortcuts import render
from datetime import datetime


def blog_details(request):
    post = {
        "title": "My Second Blog Post",
        "author": "Sangam Puri",
        "content": "This is the content of my second blog post.",
        "created_at": datetime.now(),
        "tags": ["django", "python", "web development"],
        "price":100,
        "number":7,
    }
    return render(request, 'blog/blog_details.html', {"post":post})
