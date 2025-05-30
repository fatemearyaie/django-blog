from django.contrib import admin
from .models import article, category
# CATEGORY
def StatusTrue(modeladmin, request, queryset):
    row_update = queryset.update(status=True)
    if row_update == 1:
        message_bit = "۱ نمایش داده شد"
    else:
        message_bit = f"{row_update} کتگوری نمایش داده شدند"
    modeladmin.message_user(request, message_bit)
StatusTrue.short_description = "نمایش کتگوری های انتخاب شده"

def StatusFalse(modeladmin, request, queryset):
    row_update = queryset.update(status=False)
    if row_update == 1:
        message_bit = "۱ پنهان داده شد"
    else:
        message_bit = f"{row_update} کتگوری پنهان شدند"
    modeladmin.message_user(request, message_bit)
StatusFalse.short_description = "پنهان کردن کتگوری های انتخاب شده"

class categoryadmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status', 'parent')
    list_filter = [('status')]
    search_fields = ('title', 'slug')
    actions = [StatusTrue, StatusFalse]
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':['title']}

admin.site.register(category, categoryadmin)

# ARTICLE
def make_published(modeladmin, request, queryset):
    row_update = queryset.update(status='P')
    if row_update == 1:
        message_bit = "۱ مقاله منتشر شد"
    else:
        message_bit = f"{row_update} مقاله منتشر شدند"
    modeladmin.message_user(request, message_bit)
make_published.short_description = "انتشار مقالات انتخاب شده"

def make_draft(modeladmin, request, queryset):
    row_update = queryset.update(status='D')
    if row_update == 1:
        message_bit = "۱ مقاله پیش‌نویس شد"
    else:
        message_bit = f"{row_update} مقاله پیش‌نویس شدند"
    modeladmin.message_user(request, message_bit)
make_draft.short_description = "پیش‌نویس مقالات انتخاب شده"

class articleadmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag','slug','jpublish','status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'slug')
    # generate slug field for every title automatically.
    prepopulated_fields = {'slug':['title']}
    ordering = ['status', 'publish']
    actions = [make_published, make_draft]
    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category.all()])
    
admin.site.register(article, articleadmin)