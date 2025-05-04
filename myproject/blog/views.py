from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import article
# Create your views here.
def home(request):
    context ={
        "articles": article.objects.filter(status = 'P').order_by('-publish')
        
    }
    return render(request, "blog/home.html", context)  
def api(request):
    return(JsonResponse({"title":"hi"}))

def article_detail(request, slug):
    context ={
        "article": article.objects.get(slug = slug)
        
    }
    return render(request, "blog/detail.html", context) 