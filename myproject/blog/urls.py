from django.urls import path
from .views import home, about, contact, sample, post

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('articles/<slug:slug>',post, name='post'), # <type:name>
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', sample, name='post')
]
