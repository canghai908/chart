# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from cacti.models import health

def show(request):
    hosts = health.objects.all()
    return render_to_response('show.html',{'hosts':hosts})
