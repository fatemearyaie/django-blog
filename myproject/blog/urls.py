from django.urls import path
from .views import home, article_detail, about, contact, sample

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('article/<slug:slug>',article_detail, name='detail'), # <type:name>
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', sample, name='post')
]
