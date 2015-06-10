from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bbc.models import Study, Biobank


def home_page(request):
    # biobank = Biobank.objects.create()
    # Study.objects.create(name='study1', biobank=biobank)
    # Study.objects.create(name='study2', biobank=biobank)
    return render(request, 'home.html')

def study(request, study_id=None):
    if study_id is not None:
        study = Study.objects.all().filter(id=study_id).first()
        return render(request, 'study.html', {
            'study': study
        })
    else:
        study_search(request)

def study_search(request):
    token = request.GET.get('text_search', '')
    studies = Study.objects.all().filter(name__contains=token)
    return render(request, 'studies.html', {
        'text_search': token,
        'studies': studies
    })

def biobank(request):
    biobanks = Biobank.objects.all()
    return render(request, 'biobanks.html', {
        'biobanks': biobanks
    })

def biobank_details(request, biobank_id=None):
    bb = Biobank.objects.get(id=biobank_id)
    studies = Study.objects.all().filter(biobank=bb)
    return render(request, 'biobank_details.html', {
        'biobank': bb,
        'studies': studies,
    })
