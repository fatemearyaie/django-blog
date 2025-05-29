from django.urls import path
from .views import about, contact, sample, post, category_view, ArticleList

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('articles/<slug:slug>',post, name='post'), # <type:name>
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', sample, name='post'),
    path('category/<slug:slug>/page/<int:page>', category_view, name='category')
]
