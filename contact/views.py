from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Code inspired from http://www.learningaboutelectronics.com/Articles/How-to-create-a-contact-form-for-website-in-Django.php

def contactview(request):
    name = ''
    email = ''
    message = ''

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message =form.cleaned_data.get("message")

        if request.user.is_authenticated():
            subject = str(request.user) + "'s Comment"
        else:
            subject = "A user's message"


        message = name + " with the email, " + email + ", sent the following message:\n\n" + comment;
        send_mail(subject, message, from_email, 'amiejohnstone18@gmail.com', recipient_list, [amiejohnstone18@gmail.com])


        context = {'form': form}

        return render(request, 'contact/contact.html', context)

    else:
        context = {'form': form}
        return render(request, 'contact/contact.html', context)