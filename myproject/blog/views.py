from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import article



# Create your views here.
def home(request):
    articles = article.objects.all()
    return render(request, "blog/home.html", {"articles": articles}) 

def post(request, slug):
    articleone = article.objects.get(slug = slug) # first slug is for database's field and second is for the slug we pass
    return render(request, "blog/post.html", {"article": articleone}) 

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def sample(request):
    return render(request, 'blog/post.html')