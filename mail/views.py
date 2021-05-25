from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

send_mail(
    'Sending mail',
    'Here is the message.',

    'mayasamudre@gmail.com',
    ['mayasamudre@gmail.com'],
    fail_silently=False,)
'''
import sys
sys.exit(0)
def sendemail(request):
    workerlist=Worker.objects.all()
    return render(request, '邮件发送.html',{'workerlist':workerlist})


def email(request):
    workerlist = Worker.objects.all()
    toemail = request.POST.get('toemail')
    subject = request.POST.get('subject')
    content = request.POST.get('content')
    try:
        send_mail(subject, content, 'yifzhou@163.com', [toemail])
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return render(request, '邮件发送.html',{'workerlist':workerlist})'''