import imp
from django.shortcuts import render
from Register.models import Registration
from django.contrib import messages

def Insertrecord(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('moodle_id') and request.POST.get('email_id') and request.POST.get('password'):
            saverecord=Registration()
            saverecord.name=request.POST.get('name')
            saverecord.moodle_id=request.POST.get('moodle_id')
            saverecord.email_id=request.POST.get('email_id')
            saverecord.password=request.POST.get('password')
            saverecord.save()
            messages.success(request,'record saved successfully!!!')
            return render(request,'final_login_html.html')

    else:
            return render(request,'final_login_html.html')