from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import article



# Create your views here.
def home(request):
    return render(request, "blog/home.html")  
def api(request):
    return(JsonResponse({"title":"hi"}))

def article_detail(request, slug):
    context ={
        "article": article.objects.get(slug = slug) # first slug is for database's field and second is for the slug we pass
        
    }
    return render(request, "blog/single.html", context) 