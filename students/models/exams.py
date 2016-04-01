# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Exams(models.Model):
    """
    Exam model
    """

    class Meta(object):

        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"


    exam_title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name = u"Назва дисципліни")

    exam_executor = models.ForeignKey('Professor',
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")

    exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        max_length=256,
        blank=False,
        default='')


    room = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Аудиторія")

    date_time = models.DateTimeField(
        blank=False,
        verbose_name=u"Час проведення",
        null=True)


    def __unicode__(self):
        return u"%s %s" % (self.exam_title, self.exam_executor)