from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User




def IndexView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "main/index.html", context)



def SignUpView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "main/sign_up.html", context)



def SignInView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "main/sign_in.html", context)




