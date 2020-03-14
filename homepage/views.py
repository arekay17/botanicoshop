from django.shortcuts import render
from .models import CarouselDesktop
from django.http import Http404

# Create your views here.

def home(request):
    try:
        carousel_desktop = CarouselDesktop.objects.all()[:3]
    except CarouselDesktop.DoesNotExist:
        raise Http404("Error 404")
    context = {
        'carousel_desktop' : carousel_desktop,
    }
    return render(request, 'homepage/home.html', context)