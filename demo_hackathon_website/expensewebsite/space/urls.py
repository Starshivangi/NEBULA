from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('water_temp_dashboard/', views.water_temp_dashboard, name='water_temp_dashboard'),
    path('ocean_depletion/', views.ocean_depletion, name='ocean_depletion'),
    path('quiz_for_wizz/', views.quiz_for_wizz, name='quiz_for_wizz'),
    path('pace_satellite/', views.pace_satellite, name='pace_satellite'),
    path('chlorophyll_analysis/', views.chlorophyll_analysis, name='chlorophyll_analysis'),
    path('space_dodger/', views.space_dodger, name='space_dodger'),
    path('contact/', views.contact_view, name='contact'),
    path('star_map/', views.star_map, name='star_map'),

]



