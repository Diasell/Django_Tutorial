# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from studentsdb.settings import ADMIN_EMAIL


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label=u'Ваш email'
    )

    subject = forms.CharField(
        label=u'Заголовок листа',
        max_length=256
    )

    message = forms.CharField(
        label=u'Текст повідомлення',
        max_length=2560,
        widget=forms.Textarea
    )

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
                message = u'Під час відправки листа виникла непередбачувана помилка.' \
                          u' Спробуйте скористатись даною формою пізніше.'
                messages.warning(request,message)
            else:
                message = u'Повідомлення успішно надіслане!'
                messages.success(request,message)

            # redirect to same contact page with  message
            return HttpResponseRedirect(reverse('contact_admin'))
        else:
            message = u'Будь ласка заповніть поля форми'
            messages.warning(request,message)

        # if there was not POST render blank form
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})



