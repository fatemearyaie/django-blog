from django.contrib import admin
from .models import article, category

def make_published(modeladmin, requuest, queryset):
    queryset.update(status='P')
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, requuest, queryset):
    queryset.update(status='D')
make_draft.short_description = "پیش نویس مقالات انتخاب شده"


class categoryadmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status', 'parent')
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
    actions = [make_published, make_draft]
    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category.all()])

    
# Register your models here.
admin.site.register(article, articleadmin)

    


    