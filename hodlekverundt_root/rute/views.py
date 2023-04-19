from django.shortcuts import render
from django.http import HttpResponse
from rute.models import Rute
from django.templatetags.static import static



def alle_ruter(request):
    #spør database om alle ruter
    ruter = Rute.objects.all()

    return render(request, 'rute/alle_ruter.html', {'ruter': ruter})

    #return render(request, 'rute/alle_ruter.html')

def rute_detail(request, pk):
    #spør database om rute med id=pk
    rute = Rute.objects.get(pk=pk)

    return render(request, 'rute/rute_detail.html', {'rute': rute})

def kart(request):
    gpx_file_url = 'https://raw.githubusercontent.com/jhaalbu/hodlekverundt/main/Hodlekve_rundt_2022.gpx'   # Replace with the actual GPX file path
    context = {'gpx_file_url': gpx_file_url}
    return render(request, 'rute/kart.html', context)

def kart2(request):
    gpx_file_url = static('rute/gpx/Helleberget_med_badepause.gpx')   # Replace with the actual GPX file path
    context = {'gpx_file_url': gpx_file_url}
    return render(request, 'rute/kart2.html', context)

def kart3(request):
    return render(request, 'rute/rute_kart.html')