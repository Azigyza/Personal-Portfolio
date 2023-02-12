from django.contrib import admin
from django.urls import path
from . import views         # this imports from views

app_name = 'blog'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.all_blogs,  name='all_blogs'),
    # this allows us to display blogs on their own pages
    path('<int:blog_id>/', views.detail,  name='detail'), # you alsoe have to create a render request in views
]
