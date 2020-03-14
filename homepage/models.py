from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class CarouselDesktop(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    picture = ProcessedImageField(upload_to='carousel_desktop', processors=[ResizeToFill(1280,720)], format="JPEG", options={'quality':70})

    def __str__(self):
        return self.title