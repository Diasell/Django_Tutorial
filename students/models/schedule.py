# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class WorkingDay(models.Model):

    class Meta(object):
        verbose_name = u"День тижня"
        verbose_name_plural = u"Дні тижня"

    dayoftheweek = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.dayoftheweek


class ParaTime(models.Model):

    class Meta(object):
        verbose_name = u"Час проведення пари"
        verbose_name_plural = u"Час проведення пар"

    para_starttime = models.TimeField(blank=True, null=True, verbose_name=u"Початок пари")
    para_endtime = models.TimeField(blank=True, null=True, verbose_name=u"Кінець пари")
    para_position = models.IntegerField(blank=True, null=True, default=0, verbose_name=u"Номер пари")

    def __unicode__(self):
        return u"%s: %s-%s" % (self.para_position, self.para_starttime, self.para_endtime)


class Para(models.Model):

    class Meta(object):
        verbose_name = u"Пара"
        verbose_name_plural = u"Пари"

    para_subject = models.ForeignKey('Disciplines', blank=True, null=True, verbose_name=u"Дисципліна")
    para_room = models.ForeignKey('Rooms', blank=True, null=True, verbose_name=u"Аудиторія")
    para_professor = models.ForeignKey('Professor', blank=True, null=True, verbose_name=u"Лектор")
    para_number = models.ForeignKey('ParaTime', blank=True, null=True, verbose_name=u"Номер пари")
    para_day = models.ForeignKey(WorkingDay, blank=True, null=True, verbose_name=u"День проведення")
    para_group = models.ForeignKey('Group', blank=True, null=True, verbose_name=u"Група")
    week_type = models.BooleanField(default=True, verbose_name=u"Парний тиждень")

    def __unicode__(self):
        return u"%s %s" % (self.para_subject, self.para_room)



class StartSemester(models.Model):

    class Meta(object):
        verbose_name = u"Початок семестру"
        verbose_name_plural = u"Початок семестрів"

    title = models.CharField(max_length=255,
                             blank=False,
                             null=True,
                             default=u"1 семестр",
                             verbose_name=u"Семестр")
    semesterstart = models.DateField(verbose_name=u"Дата початку навчання")
    semesterend = models.DateField(verbose_name=u"Дата закінчення навчання")

    def __unicode__(self):
        return u"%s" % self.title


