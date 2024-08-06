from django.urls import path
from . import views

urlpatterns =  [
    path("posts", views.posts),
    path("posts/<str:post>", views.post),
    path("",views.index)
]