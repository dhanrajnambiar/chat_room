from django.urls import path, re_path

from . import views

urlpatterns = [
    path('post/', views.post, name = 'post_message'),
]
