from django.http import Http404
class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'author', 'slug', 'category', 'description', 'thumbnail', 'publish', 'status']
        elif request.user.is_author:
            self.fields = ['title', 'slug', 'category', 'description', 'thumbnail', 'publish']
        else:
            raise Http404
            