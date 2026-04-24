from django.shortcuts import render
from .models import Projeto, Skill

# Create your views here.
def home(request):
    projetos = Projeto.objects.all()
    skills = Skill.objects.all()

    return render(request, 'core/pages/home.html',context={
        'projetos': projetos,
        'skills': skills,
    })
