from django.db import models
from django.urls import reverse


# Create your models here.


class Painting(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField()
    full_description = models.TextField()
    image = models.ImageField(upload_to="paintings/")
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("painting", kwargs={"slug": self.slug})

