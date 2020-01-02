from django.urls import path

from .views import MovieViews

urlpatterns = [
    path('movie/', MovieViews.as_view(), name='movie')
]
