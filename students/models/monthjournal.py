# -*- coding: utf-8 -*-
from django.db import models
from .students import Student


class MonthJournal(models.Model):
    """ Student monthly test journal"""
    class Meta:
        verbose_name = u"Журнал Відвідувань"
        verbose_name_plural = u"Журнали Відвідувань"

    student = models.ForeignKey('Student',
            verbose_name=u"Студент",
            blank=False,
            unique_for_month='date'
    )

    # we need only year and month so always set day to first of the month

    date = models.DateField(
        verbose_name=u"Дата",
        blank=False
    )

    # list of days, each says whether student was present ot not

    local_vars = locals()
    for num in range(1, 32):
        local_vars.update({'present_day' + str(num): models.BooleanField(default=False)})


    def __unicode__(self):
        return u"%s: %d, %d" % (self.student.last_name, self.date.month, self.date.year)