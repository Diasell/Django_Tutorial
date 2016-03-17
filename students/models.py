# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    """
    Students model
    """

    class Meta(object):

        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"


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
        blank=True,
        verbose_name=u"По-батькові",
        default= '')

    student_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True)

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

    ticket = models.CharField(
        blank=False,
        max_length=256,
        verbose_name=u"№ Білета‚")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Group(models.Model):

    """Group Model"""

    class Meta(object):
        verbose_name = u"Група"
        verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва групи")

    leader = models.OneToOneField('Student',
        verbose_name=u"Староста",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __unicode__(self):

        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,self.leader.last_name)
        else:
            return u"%s" % (self.title,)


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