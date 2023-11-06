from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaintingsView.as_view(), name='home'),
    path("painting/<slug:slug>", views.painting, name="painting"),
]