from django.contrib import admin
from .models import article

class articleadmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status')
    list_filter = ('publish', 'status')
<<<<<<< HEAD
    search_fields = ('title', 'slug')
=======
>>>>>>> 3cff1057982f26e58bd9ace26130bc9f806d6f31
# Register your models here.
admin.site.register(article, articleadmin)

    