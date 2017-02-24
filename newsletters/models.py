from __future__ import unicode_literals

from uuid import uuid4

from django.db import models
from django.db.models.signals import pre_save


class Join(models.Model):
    email = models.EmailField(null=False, blank=False, unique=True)
    ref_id = models.CharField(max_length=20, unique=True)
    ip_address = models.CharField(max_length=100, default='0.0.0.0')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.email


def create_uid(instance):
    uuid = str(uuid4())[:12].replace('-','').lower()
    exists = Join.objects.filter(ref_id=uuid)
    if exists:
        return create_uid(instance)
    return uuid


def pre_save_join_receiver(sender, instance, *args, **kwargs):
    if not instance.ref_id:
        instance.ref_id = create_uid(instance)


pre_save.connect(pre_save_join_receiver, sender=Join)
