from django.contrib import admin
from .models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'img', 'date')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'body', 'created_on')


admin.site.register(Comment, CommentAdmin)
