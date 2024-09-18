from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import CV

# Create your views here.
def index(request):
    cvs = CV.objects.all()
    context = {
        "cvs": cvs
    }
    return render(request, 'cv/index.html', context)

def detail(request, cv_id):
    try:
        cv = get_object_or_404(CV, pk=cv_id)
    except cv.DoesNotExist:
        raise Http404("CV does not exist")
    return render(request, 'cv/detail.html', {"cv": cv})