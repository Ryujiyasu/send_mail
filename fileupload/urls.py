from django.urls import path

from . import views

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('gmail/',views.gmail),
    path('addfile/', views.addfile_upload, name='addfile_upload'),

]