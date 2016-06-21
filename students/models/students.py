# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

# Create your models here.

class Student(models.Model):
    """
    Students model
    """

    class Meta(object):

        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"

    user = models.OneToOneField(User, primary_key=True)

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

    def __unicode__(self):
        return u"user:%s, %s %s" % (self.user, self.user.first_name, self.user.last_name)
