from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models
# Create your views here.


class PaintingsView(ListView):
    model = models.Painting
    template_name = "gallery/index.html"
    context_object_name = 'paintings'
    extra_context = {"title": "Картинная галерея Эжена Делакруа"}


class PaintingView(DetailView):
    model = models.Painting
    template_name = "gallery/painting.html"
    context_object_name = "painting"
    extra_context = {"title": "Картинная галерея Эжена Делакруа"}
    slug_url_kwarg = "slug"


def painting(request, slug):
    paint = models.Painting.objects.get(slug=slug)
    total = models.Painting.objects.count()
    all_paintings = models.Painting.objects.all()

    for ind, item in enumerate(all_paintings):
        if item == paint:
            pos = ind
            break

    return render(request,
                  "gallery/painting.html",
                  {
                      "title": "Картинная галерея Эжена Делакруа",
                      "painting": paint,
                      "prev_painting": all_paintings[(pos+total-1)%total],
                      "next_painting": all_paintings[(pos+total+1)%total]
    })
