from django.urls import path
from .import views

urlpatterns = [
    path('', views.studentform),
    path('showresult/', views.showresult),
]
