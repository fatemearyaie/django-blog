from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import article, category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404

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
    model = article
    context_object_name = 'articles'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return article.objects.all()
        else:
            return article.objects.filter(author=self.request.user) #if the author is that specific user who logged in

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

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = article
    fields = ['title', 'author', 'slug', 'category', 'description', 'thumbnail', 'publish', 'status']
    template_name = 'registeration/article-create-update.html'
    success_url = reverse_lazy('blog:create')
    
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        if getattr(self.request.user, 'is_author', False):
            for field in ['author', 'status']:
                if field in form.fields:
                    del form.fields[field]
        elif not self.request.user.is_superuser:
            raise Http404
        return form

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = article
    fields = ['title', 'author', 'slug', 'category', 'description', 'thumbnail', 'publish', 'status']
    template_name = 'registeration/article-create-update.html'
    success_url = reverse_lazy('blog:profile')
    
    def get_form(self, query_set=None):
        obj = super().get_form(query_set)
        if self.user.is_superuser:
            return obj
        elif getattr(self.request.user, 'is_author', False) and obj.author == self.request.user:
            return obj
        else:
            raise Http404("شما اجازه ویرایش این مقاله را ندارید")
        
    def get_form(self, form_class = None):
        form = super().get_form(form_class)
        if getattr(self.request.user, 'is_author', False):
            for field in ['author', 'status']:
                if field in form.fields:
                    del form.fields[field]
        elif not self.request.user.is_superuser:
            raise Http404
        return form
    

class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = article
    template_name = 'registeration/delete.html'
    success_url = reverse_lazy('blog:profile')

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            return qs
        return qs.filter(author=self.request.user)
    
    