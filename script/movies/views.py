from django.shortcuts import render
from django.http import HttpResponse


def bilo_sta(request):
    return HttpResponse('Otvorio si bilo sta stranicu')


def requested_num(request, number):
    return HttpResponse('Trazio si br: ' + str(number))


def regex(request, godina, mesec):
    return HttpResponse('Godina: ' + str(godina) + ' i mesec ' + str(mesec))


def main(request):
    return render(request, 'pages/main.html')
