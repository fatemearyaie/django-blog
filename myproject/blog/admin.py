from django.contrib import admin
from .models import article

class articleadmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status')
# Register your models here.
admin.site.register(article, articleadmin)

    