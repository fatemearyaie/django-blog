from django.contrib import admin
from .models import article, category

class articleadmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status',)
    list_filter = ('publish', 'status')
    search_fields = ('title', 'slug')
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':['title']}
    ordering = ['status', 'publish']

    
# Register your models here.
admin.site.register(article, articleadmin)

    
class categoryadmin(admin.ModelAdmin):
    list_display = ('title','slug','status', 'position')
    list_filter = [('status')]
    search_fields = ('title', 'slug')
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':['title']}

    
# Register your models here.
admin.site.register(category, categoryadmin)

    