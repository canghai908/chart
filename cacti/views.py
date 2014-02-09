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
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			User.objects.create(username = username,password = password)
			return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render_to_response('regist.html',{'uf':uf})
def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid();
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = User.objects.filter(username__exact = username, password_exact = password)
			if user:
				request.session['username'] = username
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render_to_response('login.html',{'uf':uf})
def index(request):
	username = request.session.get('username','anybody')
	return render_to_response('index.html',{'username':username})
def logout(request):
	session = request.session.get('username',False)
	if session:
		del request.session['username']
		return render_to_response('login.html',{'username':username})
	else:
		return HttpResponse('please login!')
