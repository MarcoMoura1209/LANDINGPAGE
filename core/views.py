from django.shortcuts import render
from .models import Projeto, Skill
from .forms import Form


# Create your views here.
def home(request):
    projetos = Projeto.objects.all()
    skills = Skill.objects.all()

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'core/pages/home.html', context={
        'projetos': projetos,
        'skills': skills,
        'form': form,
    },)
