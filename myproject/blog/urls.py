from django.urls import path
from .views import home, api, article_detail

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('api', api, name="api"),
    path('article/<slug:slug>',article_detail, name='detail'),
]
