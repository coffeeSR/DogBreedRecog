from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', home, name = "home"),
    path('about/',views.about_page, name='about'),
    path('members/',views.members_grp, name = 'members'),
]
