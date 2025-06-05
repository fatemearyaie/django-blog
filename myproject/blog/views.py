from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import article, category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CostumLoginView(LoginView):
    template_name = 'registeration/login.html'
    def get_success_url(self):
        if self.user.is_superuser:
            return reverse_lazy('registeration/home.html')
        else:
            return reverse_lazy('blog/article_list.html')
# Create your views here.
class ArticleList(ListView):
    context_object_name = 'articles'
    queryset = article.objects.published()
    paginate_by = 4

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(article.objects.published(), slug = slug)
    

def about(request):
    return render(request, 'blog/about.html')

def paneladmin(request):
    return render(request, 'registeration/home.html')

def contact(request):
    return render(request, 'blog/contact.html')

def sample(request):
    return render(request, 'blog/post.html')


class ArticleListAdmin(LoginRequiredMixin, ListView):
    template_name = 'registeration/home.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            article.objects.all()
        else:
            article.objects.filter(author=self.request.user) #if the author is that specific user who logged in

class CategoryList(ListView):
    paginate_by = 4
    template_name = 'blog/category_list.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(category.objects.CategoryStatus(), slug=slug)
        return category.articles.published()
    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorList(ListView):
    paginate_by = 4
    template_name = 'blog/article_list.html'
    def get_queryset(self):
        global author
        slug = self.kwargs.get('username')
        self.author = get_object_or_404(User, username=slug)
        return self.author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context
    
