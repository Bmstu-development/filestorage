from django.contrib import admin
from . import models


@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author'
