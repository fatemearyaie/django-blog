from django.urls import path
from .views import about, contact, sample, ArticleList, ArticleDetail, CategoryList,AuthorList,login

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    path('articles/<slug:slug>',ArticleDetail.as_view(), name='post'), # <type:name>
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', sample, name='post'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),
    path('account/login/', login, name='login'),

]
