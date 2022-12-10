from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/questionary.html')

def xr_app(request):
    return render(request, 'home/touch_gestures_page.html')