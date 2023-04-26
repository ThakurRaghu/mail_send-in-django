from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'index.html')


def mail(request):
    if request.method == 'POST':
        subject = 'Hello simran'
        msg = "Welcome to mail server in Django"
        to  = request.POST.get('email')
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

        if(res == 1):
            msg = 'Mail Send Successfully'
        else:
            msg="Mail could not sent"
        return HttpResponse(msg)
    return render(request, 'index.html')