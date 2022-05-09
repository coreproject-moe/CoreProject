from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class FAQModel(models.Model):
    content = RichTextUploadingField()

    def __str__(self):
        return self.content
