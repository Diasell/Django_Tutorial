# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LectorPositions(models.Model):
    """
    model for lectors position(v4ene zvannya)
    """

    class Meta(object):

        verbose_name = u"Вчене звання"
        verbose_name_plural = u"Вчені звання"

    lector_position = models.CharField(
        verbose_name=u"Вчене звання",
        blank=False,
        max_length=50)

    def __unicode__(self):
        return u"%s" % (self.lector_position)