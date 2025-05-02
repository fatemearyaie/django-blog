from django.db import models
from django.utils import timezone

# Create your models here.
class article(models.Model):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True) #اون بخشی از url که تغییر میکنه رو میگیم اسلاگ 
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    upldated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
