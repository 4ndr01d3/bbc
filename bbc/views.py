from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def study(request,study_id=None):
    token =request.POST.get('text_search', '')
    if token == "non_defined_study":
        token = ""
    if study_id:
        return HttpResponse("test_study");
    else:
        return render(request, 'study.html', {
            'text_search': token,
        })
