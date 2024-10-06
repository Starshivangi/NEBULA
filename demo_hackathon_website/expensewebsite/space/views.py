from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'index.html')

def water_temp_dashboard(request):
    return render(request, 'water_temp_dashboard.html')

def ocean_depletion(request):
    return render(request, 'ocean_depletion.html')

def quiz_for_wizz(request):
    return render(request, 'quiz_for_wizz.html')

def pace_satellite(request):
    return render(request, 'pace_satellite.html')

def chlorophyll_analysis(request):
    return render(request, 'chlorophyll_analysis.html')

def space_dodger(request):
    return render(request, 'space_dodger.html')

def contact_view(request):
    return render(request, 'contact.html')

def star_map(request):
    return render(request, 'star_map.html')
