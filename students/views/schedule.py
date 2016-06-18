# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from ..util import get_current_group, ifweekiseven

from ..models.groups import Group
from ..models.schedule import WorkingDay, Para, StartSemester

import datetime


class ScheduleView(TemplateView):
    template_name = 'students/students_schedule.html'

    def get_context_data(self, **kwargs):

        context = super(ScheduleView, self).get_context_data(**kwargs)

        # check if we need to show only 1 group of students:
        current_group = get_current_group(self.request)
        current_weekday = datetime.date.today().weekday()  # integer 0-monday .. 6-Sunday
        weekdays = ['Понеділок', "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        current_day = WorkingDay.objects.filter(dayoftheweek=weekdays[current_weekday])
        monday = WorkingDay.objects.filter(dayoftheweek=weekdays[0])
        tuesday = WorkingDay.objects.filter(dayoftheweek=weekdays[1])
        wednesday = WorkingDay.objects.filter(dayoftheweek=weekdays[2])
        thursday = WorkingDay.objects.filter(dayoftheweek=weekdays[3])
        friday = WorkingDay.objects.filter(dayoftheweek=weekdays[4])
        saturday = WorkingDay.objects.filter(dayoftheweek=weekdays[5])
        sunday = WorkingDay.objects.filter(dayoftheweek=weekdays[6])
        # checking what weektype it is now:
        todaysdate = datetime.date.today()
        semesters = StartSemester.objects.all()
        approxsemesterlength = 5*31
        for semester in semesters:
            difference = (todaysdate - semester.semesterstart).days
            if semester.semesterstart <= todaysdate and difference < approxsemesterlength:
                startsemesterdate = semester.semesterstart
                weektype = ifweekiseven(todaysdate, startsemesterdate)
            else:
                # if weektype is not recognized - uses True as default
                weektype = True

        if current_group:
            sched_today = Para.objects.filter(para_group=current_group, para_day=current_day, week_type=weektype)
            sched_monday = Para.objects.filter(para_group=current_group, para_day=monday, week_type=weektype)
            sched_tuesday = Para.objects.filter(para_group=current_group, para_day=tuesday, week_type=weektype)
            sched_wednesday = Para.objects.filter(para_group=current_group, para_day=wednesday, week_type=weektype)
            sched_thursday = Para.objects.filter(para_group=current_group, para_day=thursday, week_type=weektype)
            sched_friday = Para.objects.filter(para_group=current_group, para_day=friday, week_type=weektype)
            sched_saturday = Para.objects.filter(para_group=current_group, para_day=saturday, week_type=weektype)
            # ordering
            sched_today = sched_today.order_by('para_number__para_position')
            sched_monday = sched_today.order_by('para_number__para_position')
            sched_tuesday = sched_today.order_by('para_number__para_position')
            sched_wednesday = sched_today.order_by('para_number__para_position')
            sched_thursday = sched_today.order_by('para_number__para_position')
            sched_friday = sched_today.order_by('para_number__para_position')
            sched_saturday = sched_today.order_by('para_number__para_position')
        else:
            # TODO: what needs to be shown here if group is not defined?
            sched_today = Para.objects.all()

        context['weekday'] = current_day
        context['sched_today'] = sched_today
        # context['sched_monday'] = sched_monday
        # context['sched_tuesday'] = sched_tuesday
        #context['sched_wednesday'] = sched_wednesday
        #context['sched_thursday'] = sched_thursday
        #context['sched_friday'] = sched_friday
        #context['sched_saturday'] = sched_saturday
        context['groups'] = Group.objects.all().order_by('title')
        return context
