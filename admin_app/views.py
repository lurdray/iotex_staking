from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from app.models import AppUser
from stake.models import Stake
import datetime

def IndexView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if app_user.user.username == "admin@iotexchartapp.com":
		if request.method == "POST":
			pass

			
		else:
			stakes = Stake.objects.order_by('-pub_date')
			context = {"stakes": stakes}
			return render(request, "admin_app/index.html", context)

	else:
		return HttpResponse(str("Error, please contact Admins!"))



def StakingDetailView(request, staking_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if app_user.user.username == "admin@iotexchartapp.com":
		if request.method == "POST":
			stake = Stake.objects.get(id=staking_id)
			amount = request.POST.get("amount")
			wallet_address = request.POST.get("wallet_address")

			txn_hash = requests.post("http://127.0.0.1:4000/send-bep/", data={
				"sender": app_user.wallet_address,
				"receiver": wallet_address, #opy receiver wallet address
				"amount": amount,
				"sender_key": app_user.wallet_key

				})

			if txn_hash:
				messages.warning(request, "Congratulations! You have approved a payment.")
				return HttpResponseRedirect(reverse("admin_app:index"))

			else:
				messages.warning(request, "Sorry! Approval did not go through successfully.")
				return HttpResponseRedirect(reverse("admin_app:staking_detail", args=[staking_id]))

			
		else:
			today_date = datetime.date.today()
			stake = Stake.objects.get(id=staking_id)

			context = {"stake": stake, "today_date": today_date}
			return render(request, "admin_app/staking_detail.html", context)

	else:
		return HttpResponse(str("Error, please contact Admins!"))