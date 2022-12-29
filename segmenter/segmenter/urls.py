from segmenter import views
from django.urls import path

urlpatterns = [
    path("segmenter", views.home)
]
