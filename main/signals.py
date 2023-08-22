from django.db.models.signals import post_save
from .models import Post, Release
from mongoengine import signals as mongo_signals
from django.dispatch import receiver
from django.utils.text import slugify


@receiver(signal=post_save, sender=Post)
def auto_slug_for_post(sender, instance, created, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()


mongo_signals.pre_save.connect(Release.pre_save, sender=Release)
