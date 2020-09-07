from django.contrib import admin
from .models import Collection, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class CollectionAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Collection, CollectionAdmin)
admin.site.register(Photo)