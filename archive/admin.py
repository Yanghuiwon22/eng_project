# from django.contrib import admin
# from .models import Archive
#
# admin.site.register(Archive)

from django.contrib import admin
from .models import Archive

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'professor', 'subject', 'student', 'created_at', 'category', 'writer')

admin.site.register(Archive, ArchiveAdmin)
