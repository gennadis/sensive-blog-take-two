from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "likes")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "post")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
