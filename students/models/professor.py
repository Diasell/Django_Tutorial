# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Professor(models.Model):
    """
    Students model
    """

    class Meta(object):

        verbose_name = u"Викладач"
        verbose_name_plural = u"Викладачі"


    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name = u"Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"По-батькові")

    position = models.ForeignKey('LectorPositions',
        max_length=256,
        blank=False,
        verbose_name=u"Вчене звання",
        on_delete=models.PROTECT)

    level = models.ForeignKey('LectorLevel',
        max_length=256,
        blank=False,
        verbose_name=u"Науковий ступінь",
        on_delete=models.PROTECT)

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)


    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __unicode__(self):
        return u"%s %s %s" % (self.last_name, self.first_name, self.middle_name)