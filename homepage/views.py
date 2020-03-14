from django.shortcuts import render
from .models import CarouselDesktop, HomeCaption, HomePictures
from django.http import Http404

# Create your views here.

def home(request):
    try:
        carousel_desktop = CarouselDesktop.objects.all()[:3]
        home_caption = HomeCaption.objects.all()
        home_pictures = HomePictures.objects.all()

    except (CarouselDesktop.DoesNotExist, HomeCaption.DoesNotExist, HomePictures.DoesNotExist ):
        raise Http404("Error 404")
    context = {
        'carousel_desktop' : carousel_desktop,
        'home_caption' : home_caption,
        'home_pictures' : home_pictures,
    }
    return render(request, 'homepage/home.html', context)