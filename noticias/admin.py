from django.contrib import admin
from .models import Noticia

class NoticeAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.

admin.site.register(Noticia, NoticeAdmin)