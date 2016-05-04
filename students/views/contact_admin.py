# -*- coding: utf-8 -*-

import logging

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

#crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from studentsdb.settings import ADMIN_EMAIL

from django.contrib.auth.decorators import permission_required

from django.utils.translation import ugettext_lazy as _

from django.utils.translation import ugettext as __


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label=_(u"Your Email")
    )

    subject = forms.CharField(
        label=_(u"Subject"),
        max_length=256
    )

    message = forms.CharField(
        label=_(u"Email message"),
        max_length=2560,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', __(u"Send")))


@permission_required('auth.add_user')
def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':

        # create a form instance and populate it with data from request:
        form = ContactForm(request.POST)

        # check whether user data is valid:
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject,message,from_email, [ADMIN_EMAIL])
            except Exception:
                message = __(u"While sending this letter unexpected error occured." \
                          u"Please try again later.")
                logger = logging.getLogger(__name__)
                logger.exception(message)
                messages.warning(request,message)
            else:
                message = __(u"Message has been sent successfully!")
                messages.success(request,message)

            # redirect to same contact page with  message
            return HttpResponseRedirect(reverse('contact_admin'))

        # if there was not POST render blank form
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})



