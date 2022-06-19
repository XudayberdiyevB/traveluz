from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Shahar')
    info = models.CharField(max_length=1000)
    about_city = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='city_images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["name"]
