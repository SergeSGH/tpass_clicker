from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'short_link',
        'original_link',
        'expires'
    )
    search_fields = ('chat_id',)


admin.site.register(Link, LinkAdmin)
