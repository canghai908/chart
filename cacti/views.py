# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from cacti.models import health,User
from django import forms

def show(request):
    hosts = health.objects.all()
    return render_to_response('show.html',{'hosts':hosts})
class UserForm(forms.Form):
	usrename = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
def regist(request):
	if request.method =="POST":
		uf = UserForm(request.POST)
		if uf.is_valid():
			usrename = uf.clean_data['username']
			