from django.contrib import admin

from .models import Blog,Category


class BlogAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'publishing_date', 'slug' ]
    list_display_links = [ 'publishing_date' ]
    list_filter = [ 'publishing_date' ]
    search_fields = [ 'title', 'content' ]
    list_editable = [ 'title' ]





admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
