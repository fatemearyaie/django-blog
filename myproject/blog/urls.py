from django.urls import path
from .views import (about,
                    contact,
                    ArticleList,
                    ArticleDetail,
                    CategoryList,
                    AuthorList,
                    ArticleListAdmin,
                    ArticleCreate,
                    ArticleUpdate,
                    ArticleDelete)
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>/', ArticleList.as_view(), name='home'),
    path('articles/<slug:slug>/',ArticleDetail.as_view(), name='post'), # <type:name>
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<slug:slug>/page/<int:page>/', CategoryList.as_view(), name='category'),
    path('author/<slug:username>/page/<int:page>/', AuthorList.as_view(), name='author'),
    path('accounts/login/', LoginView.as_view(template_name = 'registeration/login.html'),name='login'),
    path('accounts/profile/',ArticleListAdmin.as_view(), name='profile'),
    path('accounts/article/create/', ArticleCreate.as_view(), name='create'),
    path('accounts/article/update/<int:pk>/', ArticleUpdate.as_view(), name='update'),
    path('accounts/delete/<int:pk>/', ArticleDelete.as_view(), name='delete'),
    path('accounts/logout/', LogoutView.as_view(),name='logout'),

]
