from django.contrib import admin
from .models import Announcement, CarouselDesktop, HomeCaption, HomePictures

# Register your models here.

admin.site.register(Announcement)
admin.site.register(CarouselDesktop)
admin.site.register(HomeCaption)
admin.site.register(HomePictures)
