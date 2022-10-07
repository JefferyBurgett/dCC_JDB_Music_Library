from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.music_list),
    path('<int:pk>/', views.music_detail),
    path('<int:pk>/like/', views.like_song),
]