from django.urls import path

from .views import GetMovies, CommentViews, TopView, CreateMovie

urlpatterns = [
    path('movie/get', GetMovies.as_view(), name='get'),
    path('movie/create', CreateMovie.as_view(), name='create'),
    path('comment/', CommentViews.as_view(), name='comment'),
    path('top/', TopView.as_view(), name='top')
]
