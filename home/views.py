from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/questionary.html')

def xr_app(request):
    context = {}
    aux = request.POST.get('name', None)
    context['name'] = aux

    aux = request.POST.get('p1', None)
    context['p1'] = aux

    aux = request.POST.get('p2', None)
    context['p2'] = aux

    aux = request.POST.get('p3', None)
    context['p3'] = aux

    aux = request.POST.get('p4', None)
    context['p4'] = aux

    aux = request.POST.get('p5', None)
    context['p5'] = aux

    aux = request.POST.get('p6', None)
    context['p6'] = aux

    aux = request.POST.get('p7', None)
    context['p7'] = aux

    aux = request.POST.get('p8', None)
    context['p8'] = aux

    aux = request.POST.get('p9', None)
    context['p9'] = aux

    aux = request.POST.get('p10', None)
    context['p10'] = aux

    aux = request.POST.get('p11', None)
    context['p11'] = aux

    aux = request.POST.get('p12', None)
    context['p12'] = aux

    aux = request.POST.get('p13', None)
    context['p13'] = aux

    aux = request.POST.get('p14', None)
    context['p14'] = aux

    aux = request.POST.get('p15', None)
    context['p15'] = aux

    aux = request.POST.get('p16', None)
    context['p16'] = aux

    aux = request.POST.get('p17', None)
    context['p17'] = aux

    aux = request.POST.get('p18', None)
    context['p18'] = aux

    return render(request, 'home/touch_gestures_page.html', context)