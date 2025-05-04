from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import article
# Create your views here.
def home(request):
    context ={
        "articles": article.objects.all()
    }
    return render(request, "blog/home.html", context)  
def api(request):
    return(JsonResponse({"title":"hi"}))