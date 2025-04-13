from django.urls import path
from . import views

urlpatterns = [
        path('boekenlijst/', views.boekenlijst, name='boekenlijst'),
]