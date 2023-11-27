from django.contrib import admin


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date",)
    list_display = ("title", "date", "author",)


from .models import Post, Author, Tag

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
