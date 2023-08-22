from django.db import models
from django.utils.text import slugify
from django_mongoengine import Document, EmbeddedDocument, fields


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, blank=True, unique=True)


class Comment(EmbeddedDocument):
    name = fields.StringField(max_length=55)
    content = fields.StringField(verbose_name='Comment')


class Release(Document):
    title = fields.StringField(max_length=255)
    slug = fields.StringField(max_length=255, uniqe=True)
    comments = fields.ListField(
        fields.EmbeddedDocumentField('Comment'), blank=True,
    )

    @classmethod
    def pre_save(cls, sender, document, **kwargs):

        # Set Slug For Release
        if not document.slug:
            document.slug = slugify(document.title)
