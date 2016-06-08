# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Disciplines(models.Model):
    """
    model for that saves all disciplines
    """

    class Meta(object):

        verbose_name = u"Дисципліна"
        verbose_name_plural = u"Дисципліни"

    discipline = models.CharField(
        verbose_name=u"Дисципліна",
        blank=False,
        max_length=255)

    def __unicode__(self):
        return u"%s" % self.discipline
