from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bbc.models import Study, Biobank

test_data = []
def fill_dummy_data_for_tests():
    biobank1 = Biobank.objects.create(name="biobank1")
    biobank2 = Biobank.objects.create(name="biobank2")
    study1 = Study.objects.create(name="study1", biobank=biobank1)
    study2 = Study.objects.create(name="study2", biobank=biobank1)
    study3 = Study.objects.create(name="study3", biobank=biobank2)
    study4 = Study.objects.create(name="study4", biobank=biobank2)
    global test_data
    test_data=[biobank1, biobank2, study1, study2, study3, study4]

def remove_dummy_data_for_tests():
    global test_data
    for datum in test_data:
        datum.delete()
    test_data = []

def home_page(request):
    if request.GET.get('testing', '') == "create":
        fill_dummy_data_for_tests()
    if request.GET.get('testing', '') == "remove":
        remove_dummy_data_for_tests()
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
