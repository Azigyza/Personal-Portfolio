from django.contrib import admin
from django.urls import path
from . import views         # this imports from views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_blogs,  name='all_blogs'),
]
