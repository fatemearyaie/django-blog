from django.db import models
from django.utils import timezone
from extensions.utils import jalaliConvertor
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.urls import revers
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    pass

# manager 
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status = "P")
    
class CategoryManager(models.Manager):
    def CategoryStatus(self):
        return self.filter(status=True)
    

# Create your models here.
class category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name='عبارت زیر دسته') #self points to category model
    title = models.CharField(max_length=50, verbose_name=" عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name='پوزیشن')

    objects = CategoryManager()
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title
    

class article(models.Model):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ") #اون بخشی از url که تغییر میکنه رو میگیم اسلاگ 
    category = models.ManyToManyField(category, verbose_name="دسته بندی", related_name='articles')
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='images', verbose_name="عکس بندانگشتی")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    objects = ArticleManager()


    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        ordering = ['publish']
    

    def __str__(self):
        return self.title
    def jpublish(self):
        return jalaliConvertor(self.publish)
    def category_published(self):
        return self.category.filter(status=True)
    def categorypublished(self):
        return self.category.filter(status = True)
    def thumbnail_tag(self):
        return format_html("<img width=100 src='{}'>".format(self.thumbnail.url))
    def category_to_str(self):
        return "، ".join([category.title for category in self.category.all()])
    def get_absolute_url(self):
        return reverse("account/profile")
    