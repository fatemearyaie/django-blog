from django.urls import path
from .views import about, contact, sample, ArticleList, ArticleDetail, CategoryList,AuthorList, paneladmin, ArticleListAdmin, ArticleCreate
from django.contrib.auth.views import LoginView

app_name = 'blog'
urlpatterns = [
    path('/', ArticleList.as_view(), name='home'),
    path('page/<int:page>/', ArticleList.as_view(), name='home'),
    path('articles/<slug:slug>/',ArticleDetail.as_view(), name='post'), # <type:name>
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<slug:slug>/page/<int:page>/', CategoryList.as_view(), name='category'),
    path('author/<slug:username>/page/<int:page>/', AuthorList.as_view(), name='author'),
    path('account/login/', LoginView.as_view(template_name = 'registeration/login.html'),name='login'),
    path('accounts/profile/',paneladmin, name='profile'),
    path('account/list/', ArticleListAdmin.as_view(), name='articlelist'),
    path('account/article/create/', ArticleCreate.as_view(), name='create')
]
