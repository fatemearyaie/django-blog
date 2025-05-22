from django.db import models
from django.utils import timezone
from extensions.utils import jalaliConvertor


# manager 
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status = "P")
# Create your models here.

class category(models.Model):
    title = models.CharField(max_length=50, verbose_name=" عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title

class article(models.Model):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published')
    )
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ") #اون بخشی از url که تغییر میکنه رو میگیم اسلاگ 
    category = models.ManyToManyField(category, verbose_name="دسته بندی")
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='images', verbose_name="عکس بندانگشتی")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"
        ordering = ['-publish']
    

    def __str__(self):
        return self.title
    def jpublish(self):
        return jalaliConvertor(self.publish)
    def category_published(self):
        return self.category.filter(status=True)
    objects = ArticleManager()
