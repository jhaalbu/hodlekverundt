from django.shortcuts import render
from app.models import Info, Tekst, Nyheter

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def info(request):
    informasjon = Info.objects.all()
    tekst = Tekst.objects.all()
    return render(request, 'app/info.html', {'informasjon': informasjon, 'tekst': tekst})

def nyheter(request):
    nyheter = Nyheter.objects.all()
    return render(request, 'app/nyheter.html', {'nyheter': nyheter})