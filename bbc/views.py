from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bbc.models import Study


def home_page(request):
    return render(request, 'home.html')

def study(request, study_id=None):
    if study_id is not None:
        study = Study.objects.all().filter(name=study_id).first()
        return render(request, 'study.html', {
            'study': study
        })
    else:
        token = request.GET.get('text_search', '')
        studies = Study.objects.all().filter(name__contains=token)
        return render(request, 'studies.html', {
            'text_search': token,
            'studies': studies
        })

def study_search(request, study_id=None):
    token = study_id if study_id != None else request.POST.get('text_search', '')
    studies = Study.objects.all().filter(name__contains=token)

    return render(request, 'study.html', {
        'text_search': token,
        'studies': studies
    })

