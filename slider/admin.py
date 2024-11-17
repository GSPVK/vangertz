from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from easy_thumbnails.files import get_thumbnailer
from django.utils.html import format_html
from .models import SliderItem

@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_thumb', 'title', 'order')
    list_display_links = ('title',)
    search_fields = ('title',)

    def image_thumb(self, obj):
        if obj.image:
            thumbnail_url = get_thumbnailer(obj.image)['admin_preview'].url
            return format_html('<img src="{}" style="width: 100px; height: auto;">', thumbnail_url)
        return 'Нет изображения'

    image_thumb.short_description = 'Превью'