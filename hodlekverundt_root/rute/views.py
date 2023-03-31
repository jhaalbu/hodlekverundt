from django.shortcuts import render
from django.http import HttpResponse
from rute.models import Rute



def alle_ruter(request):
    #spør database om alle ruter
    ruter = Rute.objects.all()

    return render(request, 'rute/alle_ruter.html', {'ruter': ruter})

    #return render(request, 'rute/alle_ruter.html')

def rute_detail(request, pk):
    #spør database om rute med id=pk
    rute = Rute.objects.get(pk=pk)

    return render(request, 'rute/rute_detail.html', {'rute': rute})