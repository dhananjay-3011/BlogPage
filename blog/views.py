from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
    allposts = Post.objects.all()
    context = {'allposts' : allposts }
    return render(request, 'blog/blogHome.html', context)
    


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    contexts = {'post': post}
    return render(request, 'blog/blogPost.html', contexts)
   