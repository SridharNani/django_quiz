import imp
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
urlpatterns = [
    path('',index,name='index'),
    path('home/', home,name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
 
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)