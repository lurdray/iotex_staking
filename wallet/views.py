from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from app.models import AppUser
import requests


def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:

		bnb_balance = requests.get("http://127.0.0.1:4000/get-bnb-balance/%s/" % (app_user.wallet_address))
		bep_balance = requests.get("http://127.0.0.1:4000/get-bep-balance/%s/" % (app_user.wallet_address))

		bnb_balance = bnb_balance.json()
		bep_balance = bep_balance.json()
		
		context = {"bnb_balance": bnb_balance, "bep_balance": bep_balance}
		return render(request, "wallet/index.html", context)




def Send1View(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		address = request.POST.get("address")
		amount = request.POST.get("amount")

		txn_hash = requests.post("http://127.0.0.1:4000/send-bnb/", data={
			"sender": app_user.wallet_address,
			"receiver": address, #opy receiver wallet address
			"amount": amount,
			"sender_key": app_user.wallet_key

			})

		if txn_hash:
			messages.warning(request, "Congratulations! transfer was successful.")
			return HttpResponseRedirect(reverse("app:index"))

		else:
			messages.warning(request, "Sorry! transfer was not successful.")
			return HttpResponseRedirect(reverse("app:index"))

		
	else:
		
		context = {}
		return render(request, "wallet/send1.html", context)


def Send2View(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		address = request.POST.get("address")
		amount = request.POST.get("amount")

		txn_hash = requests.post("http://127.0.0.1:4000/send-bep/", data={
			"sender": app_user.wallet_address,
			"receiver": address, #opy receiver wallet address
			"amount": amount,
			"sender_key": app_user.wallet_key

			})

		if txn_hash:
			messages.warning(request, "Congratulations! transfer was successful.")
			return HttpResponseRedirect(reverse("app:index"))

		else:
			messages.warning(request, "Sorry! transfer was not successful.")
			return HttpResponseRedirect(reverse("app:index"))

	else:
		
		context = {}
		return render(request, "wallet/send2.html", context)




def ReceiveView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "wallet/receive.html", context)