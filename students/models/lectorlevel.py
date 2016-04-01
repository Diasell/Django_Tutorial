# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LectorLevel(models.Model):
    """
    model for lectors position(v4ene zvannya)
    """

    class Meta(object):

        verbose_name = u"Науковий Ступінь"
        verbose_name_plural = u"Наукові Ступені"

    lector_level = models.CharField(
        verbose_name=u"Науковий Ступінь",
        blank=False,
        max_length=50)

    def __unicode__(self):
        return u"%s" % (self.lector_level)
