from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from app.models import *
from stake.models import *
import requests

from django.utils import timezone
import datetime



def StakeView(request):
	if request.method == "POST":
		amount = request.POST.get("amount")
		app_user = AppUser.objects.get(user__pk=request.user.id)
		duration = request.POST.get("duration")

		txn_hash = requests.post("http://127.0.0.1:4000/send-bep/", data={
			"sender": app_user.wallet_address,
			"receiver": "0x7d8b40BBB42D05cbFF4696AAe83AcEdb22467100", #opy receiver wallet address
			"amount": amount,
			"sender_key": app_user.wallet_key

			})

		if txn_hash:
			stake = Stake.objects.create(app_user=app_user, amount=amount, duration=duration)
			stake.save()

			#returns block
			if duration == "14":
				returns = float(amount) + float(amount)*0.1 #10%
			elif duration == "21":
				returns = float(amount) + float(amount)*0.2 #20%
			elif duration == "30":
				returns = float(amount) + float(amount)*0.3 #30%
			else:
				returns = float(amount) + float(amount)*0.4 #40%
			stake.returns = returns

			payment_hash = txn_hash.json()
			stake.payment_hash = payment_hash["txn_hash"]
			stake.payment_status = True
			stake.payment_confirmation_status = True

			today = timezone.now().date()
			due_date = today + datetime.timedelta(days=int(duration))
			stake.due_date = due_date

			stake.save()

			messages.warning(request, "Congratulations! you have successfully staked your asset!")
			return HttpResponseRedirect(reverse("staking:my_stakes"))

		else:
			messages.warning(request, "Sorry! your staking could not go through.(Try top-up your account.")
			return HttpResponseRedirect(reverse("staking:stake"))


	else:
		
		context = {}
		return render(request, "stake/stake.html", context)




def MakePaymentView(request, staking_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":

		stake = Stake.objects.get(id=staking_id)
		
		messages.warning(request, "Congratulations! You have made pyament.")
		return HttpResponseRedirect(reverse("staking:confirm_payment", args=[stake.id,]))



	else:

		context = {}
		return render(request, "stake/make_payment.html", context)




def ConfirmPaymentView(request, staking_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		stake = Stake.objects.get(id=staking_id)

		messages.warning(request, "Congratulations! You have confirm your pyament.")
		return HttpResponseRedirect(reverse("staking:my_stakes"))

	else:

		context = {}
		return render(request, "stake/confirm_payment.html", context)



def MyStakesView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass


	else:

		my_stakes = Stake.objects.filter(app_user=app_user).order_by('-pub_date')

		context = {"my_stakes": my_stakes}
		return render(request, "stake/my_stakes.html", context)




def RequestPaymentView(request, staking_id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		stake = Stake.objects.get(id=staking_id)

		from datetime import datetime
		due_date = datetime(int(str(stake.due_date)[:4]), int(str(stake.due_date)[5:7]), int(str(stake.due_date)[8:10]))
		today_date = datetime.now()

		if today_date > due_date or today_date == due_date:
			stake.request_payment_status = True
			stake.save()

			messages.warning(request, "Congratulations! You have requested for pyament.")
			return HttpResponseRedirect(reverse("staking:my_stakes"))

		else:
			messages.warning(request, "Sorry! Unfornately, you are can not request for payment at this time.")
			return HttpResponseRedirect(reverse("staking:my_stakes"))

	else:

		stake = Stake.objects.get(id=staking_id)

		context = {"stake": stake}
		return render(request, "stake/request_payment.html", context)


