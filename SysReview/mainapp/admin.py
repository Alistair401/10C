from django.contrib import admin
from mainapp.models import Review, Query, Paper,Researcher


class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('pk','name')

class QueryAdmin(admin.ModelAdmin):
    list_display = ('pk','review')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('pk','title','review','abstract_relevance','document_relevance')

class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('user','name','surname')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(Paper, DocumentAdmin)
admin.site.register(Researcher, ResearcherAdmin)