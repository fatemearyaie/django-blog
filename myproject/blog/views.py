from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import article, category
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView



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

def contact(request):
    return render(request, 'blog/contact.html')

def sample(request):
    return render(request, 'blog/post.html')
    
def category_view(request, slug, page=1):
    categories = get_object_or_404(category, slug=slug, status = True)
    articles_list = categories.articles.published()
    paginator = Paginator(articles_list, 4) # this get the list of articles and how many of them display in each page
    articles = paginator.get_page(page) # show that articles that user requested ex:if user wants page2's articles it return the 4-8 articles
    context = {
        'category' : categories,
        'articles' : articles
    }
    return render(request, "blog/category.html", context) 
