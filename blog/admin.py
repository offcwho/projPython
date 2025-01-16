from django.contrib import admin
from blog.models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    search_fields = ['title']
    ordering = ['id']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category','is_active']
    search_fields = ['title']
    ordering = ['id']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_active', 'category']
    list_editable = ['is_active', 'category']