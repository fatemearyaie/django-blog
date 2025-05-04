from django.contrib import admin
from .models import article

class articleadmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'slug')
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':('title')}
# Register your models here.
admin.site.register(article, articleadmin)

    