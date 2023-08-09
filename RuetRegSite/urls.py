from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('teacher/login/', include('teachersite.urls')),
    path('studentsite/', include('studentsite.urls'))

]
