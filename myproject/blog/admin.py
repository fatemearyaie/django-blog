from django.contrib import admin
from .models import article, category

class categoryadmin(admin.ModelAdmin):
    list_display = ('title','slug','status', 'position', 'parent')
    list_filter = [('status')]
    search_fields = ('title', 'slug')
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':['title']}

    
# Register your models here.
admin.site.register(category, categoryadmin)


class articleadmin(admin.ModelAdmin):
    list_display = ('title','slug','jpublish','status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'slug')
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':['title']}
    ordering = ['status', 'publish']

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category.all()])

    
# Register your models here.
admin.site.register(article, articleadmin)

    


    