# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from ..util import paginate, get_current_group

from ..models.students import Student
from ..models.groups import Group
from ..models.schedule import WorkingDay, ParaTime, Para

from datetime import datetime

from django.contrib import messages
from django.views.generic import UpdateView, DeleteView

from django.forms import ModelForm, ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions



from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.utils.translation import ugettext as _



class ScheduleView(TemplateView):
    template_name = 'students/students_schedule.html'

    def get_context_data(self, **kwargs):

        context = super(ScheduleView, self).get_context_data(**kwargs)

        # check if we need to show only 1 group of students:
        current_group = get_current_group(self.request)
        current_weekday = datetime.today().weekday() # integer 0-monday .. 6-Sunday
        weekdays = ['Понеділок', "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        day = WorkingDay.objects.filter(dayoftheweek=weekdays[current_weekday])

        if current_group:
            sched_today = Para.objects.filter(para_group=current_group, para_day=day)
            #ordering
            sched_today = sched_today.order_by('para_number__para_position')
        else:
            # TODO: what needs to be shown here if group is not defined?
            sched_today=Para.objects.all()[0]


        context['weekday'] = day
        context['sched_today'] = sched_today
        context['groups'] = Group.objects.all().order_by('title')


        return context