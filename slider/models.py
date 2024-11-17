from django.db import models
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    title = models.CharField('Название', max_length=100)
    image = FilerImageField(related_name='slider_images', on_delete=models.CASCADE)
    order = models.PositiveIntegerField('Порядок', default=0, blank=False, null=False, db_index=True)  # adminsortable

    class Meta:
        ordering = ('order',)
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Элементы слайдера'

    def __str__(self):
        return self.title
