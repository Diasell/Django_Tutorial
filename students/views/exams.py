# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from ..models.exams import Exams
from ..models.groups import Group
from ..models.students import Student
from django.forms import ModelForm, ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout, Fieldset
from crispy_forms.bootstrap import FormActions

from django.contrib import messages
from django.views.generic import UpdateView

from ..util import get_current_group

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Views for Students
def exams_list(request):

    # check if we need to display exams only for 1 group that is selected
    current_group = get_current_group(request)
    if current_group:
        exams = Exams.objects.filter(exam_group=current_group)
    else:
        exams = Exams.objects.all().order_by('date_time')
    # ordering students by last_name when 1st time on the page:
    if request.path == '/':
        exams = exams.order_by('exam_group')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('exam_group', 'exam_title', 'date_time', 'exam_executor'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # paginate students
    paginator = Paginator(exams, 5)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        exams = paginator.page(paginator.num_pages)



    return render(request, 'students/exams.html',{'exams': exams,
                                                  'groups': Group.objects.all().order_by('title')})



class ExamsUpdateForm(ModelForm):

    class Meta:
        model = Exams
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ExamsUpdateForm, self).__init__(*args,**kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('exams_edit', kwargs={'pk':kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        """self.helper = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"))"""
        self.helper.layout = Layout(
            Fieldset(
                '',
                'exam_title',
                'exam_executor',
                'exam_group',
                'room',
                'date_time'
            ),
            FormActions(
                Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
                Submit('cancel_button', u'Скасувати', css_class="btn btn-link")
            )
        )



class ExamsUpdateView(UpdateView):
    model = Exams
    template_name = 'students/exams_edit.html'
    form_class = ExamsUpdateForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ExamsUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('exams')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            cancel_message = u'Редагування іспиту відмінено!'
            messages.info(request, cancel_message)
            return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!' % reverse('exams'))
        else:
            return super(ExamsUpdateView, self).post(request, *args, **kwargs)