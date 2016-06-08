# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Rooms(models.Model):
    """
    model for that saves all rooms
    """

    class Meta(object):

        verbose_name = u"Аудиторія"
        verbose_name_plural = u"Аудиторії"

    room = models.CharField(
        verbose_name=u"Аудиторія",
        blank=False,
        max_length=10)

    def __unicode__(self):
        return u"%s" % self.room
