from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from .models import SliderItem

@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_thumb', 'title', 'order')
    list_display_links = ('title',)
    search_fields = ('title',)

    def image_thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;">', obj.image.url)
        return 'Нет изображения'

    image_thumb.short_description = 'Превью'
