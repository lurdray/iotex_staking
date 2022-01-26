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

		my_stakes = Stake.objects.filter(app_user=app_user).order_by('-pub_date')
		total_staked = 0
		for item in my_stakes:
			total_staked += item.amount

		context = {"my_stakes": my_stakes, "bnb_balance": bnb_balance,
		"bep_balance": bep_balance, "wallet_address": app_user.wallet_address, "total_staked": total_staked}
		
		return render(request, "app/app.html", context)


