# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import  reverse

from ..models.groups import Group
from ..models.students import Student

from django.views.generic import UpdateView, DeleteView
from django.contrib import messages

from django.forms import ModelForm, ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

# Views for Groups
def groups_list(request):
    groups = Group.objects.all()
    # ordering groups by title by default

    if request.path == '/groups/':
        groups = groups.order_by('title')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate groups
    paginator = Paginator(groups, 3)

    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups.html', {'groups' : groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


class DeleteGroupView(DeleteView):
    model = Group
    template_name = 'students/delete_group_confirm.html'

    def get_success_url(self):
        return u'%s?Status_message=Група успішно видалена' % reverse('groups')

class GroupUpdateForm(ModelForm):

    class Meta:
        model = Group
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args,**kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse('groups_edit', kwargs={'pk':kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        self.helper.layout[-1]=FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link")
        )

    def clean_leader(self):
        """
        Check if selected student belongs to the group. If not then he cant be a leader
        of this group
        """
        # gets all students that belongs to selected group
        group_students = Student.objects.filter(student_group = self.instance)

        if len(group_students)>0 and self.cleaned_data['leader'] not in group_students:
            raise ValidationError(u"Студент не належить до даної групи", code='invalid')
        else:
            return self.cleaned_data['leader']


class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/groups_edit.html'
    form_class = GroupUpdateForm

    def get_success_url(self):

        return u'%s?status_message=Зміни успішно збережено!' % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            cancel_message = u'Редагування відмінено!'
            messages.info(request, cancel_message)
            return HttpResponseRedirect(u'%s?status_message=Редагування відмінено!' % reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)
