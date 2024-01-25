import os
from django.conf import settings
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, Http404
from .models import About, Skill, Project, FilesWord
from .forms import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import EmailMessage




# Create your views here.
def home(request):
    abouts = About.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    filesWord = FilesWord.objects.all()
    return render(request, "core/home.html",{'abouts':abouts, 'skills':skills, 'projects':projects, 'filesWord':filesWord})

def download(request, path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='imnline;filename='+os.path.basename(file_path)
            return response
        
    raise Http404

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('core/email.html', {
            'name': name,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['i.amo850426@gmail.com']
        )
        email.fail_silently = False
        email.send()

        messages.success(request, 'thank you for the email, we will contact you a soon as possible')
        return redirect('home')

