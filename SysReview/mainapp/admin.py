from django.contrib import admin
from mainapp.models import Review, Query, Paper


class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('pk','name')

class QueryAdmin(admin.ModelAdmin):
    list_display = ('pk','review')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('pk','title','review','currentPool')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(Paper, DocumentAdmin)