from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse # Add this


from .forms import ContactForm # Add this


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           sender_name = form.cleaned_data['name']
           sender_email = form.cleaned_data['email']

           message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
           send_mail('New Enquiry', message, sender_email, ['bbonsu101@gmail.com'], fail_silently=False,)
            # send email code goes here
           return HttpResponse("Thanks for contacting us!")
    else:
        form = ContactForm()

    return render(request, 'email.html', {'form': form})
#check facebook what is the way forward?
# I will go now.Keep coding.I think U got your answers
#no 
# u are accessing the emil.html page from contact/us now instead of contact-us/contact-us
#isnt the a way we can get contact-us?

