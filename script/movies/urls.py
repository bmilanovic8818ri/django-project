from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.bilo_sta, name='movies_bilo_sta'),
    path('request/<int:number>/', views.requested_num, name='movies_requested_num'),
    re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))/$',
            views.regex, name='movies_regex'),
    path('main', views.main, name='movies_main'),

    #<int:number> - route convertor koji sluzi kao validator da br mora biti int
]
