from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/ejemplo/', views.cv_ejemplo, name='cv_ejemplo'),
    path('cv/christian/', views.cv_christian, name='cv_christian'),
    path('cv/maicol/', views.cv_maicol, name='cv_maicol'),
]
