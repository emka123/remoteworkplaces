from django.db import models
from django.utils import timezone

class Place(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField('Photo', upload_to='static/photos')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title