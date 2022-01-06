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
		return render(request, "wallet/index.html", context)




def Send1View(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "wallet/send1.html", context)


def Send2View(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "wallet/send2.html", context)




def ReceiveView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "wallet/receive.html", context)