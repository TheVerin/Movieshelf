from django.urls import path

from .views import MovieViews, CommentViews

urlpatterns = [
    path('movie/', MovieViews.as_view(), name='movie'),
    path('comment/', CommentViews.as_view(), name='comment')
]
