from django.contrib import admin

from .models import Resource, Relationship
# Register your models here.
class RelationshipInline(admin.StackedInline):
    model = Relationship


class ResourceAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline,]

admin.site.register(Resource)
admin.site.register(Relationship)
