from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import article, category



# Create your views here.
def home(request):
    context = {
        "articles" : article.objects.published(),
        "categories" : category.objects.CategoryStatus()
               }

    return render(request, "blog/home.html", context) 

def post(request, slug):
    articleone = article.objects.get(slug = slug) # first slug is for database's field and second is for the slug we pass
    return render(request, "blog/post.html", {"article": articleone}) 

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def sample(request):
    return render(request, 'blog/post.html')
    
def category(request, slug):
    context = {
        'category' : get_object_or_404(category, slug=slug, status = True),
    }
    return render(request, "blog/category.html", context) 
