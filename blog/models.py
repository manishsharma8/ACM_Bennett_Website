from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    profile_pic = models.ImageField(upload_to = 'images/')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.TimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title