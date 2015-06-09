from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from bbc.models import Study


def home_page(request):
    return render(request, 'home.html')

def study(request, study_id=None):
    token = study_id if study_id != None else request.POST.get('text_search', '')
    studies = Study.objects.all().filter(name__contains=token)

    return render(request, 'study.html', {
        'text_search': token,
        'studies': studies
    })


