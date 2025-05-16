from django.db import models
from django.utils import timezone
from extensions.utils import jalaliConvertor

# Create your models here.
class article(models.Model):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published')
    )
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ") #اون بخشی از url که تغییر میکنه رو میگیم اسلاگ 
    description = models.TextField(verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to='images', verbose_name="عکس بندانگشتی")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها"

    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalaliConvertor(self.publish)