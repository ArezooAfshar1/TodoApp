from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created', 'updated')
    list_filter = ('title', 'completed', 'created')
    search_fields = ('title', 'created', 'completed')
    show_facets = admin.ShowFacets.ALWAYS
