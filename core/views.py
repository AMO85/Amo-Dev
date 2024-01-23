import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import About, Skill, Project, FilesWord


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
