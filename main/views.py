from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import *

from app.models import AppUser
import requests




def IndexView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "main/index.html", context)




def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)

				app_user = AppUser.objects.get(user__pk=request.user.id)

				if app_user.user.username == "admin@iotexchartapp.com":
					print("11111111111111111111111111111111")
					messages.success(request, "Welcome Onboard Admin!")
					return HttpResponseRedirect(reverse("admin_app:index"))

				else:
					print("11111111111111111111111111111111")
					messages.success(request, "Welcome Onboard")
					return HttpResponseRedirect(reverse("app:index"))
			else:
				print("22222222222222222222222222222222")
				messages.warning(request, "Sorry, Invalid Login Details")
				return HttpResponseRedirect(reverse("main:sign_in"))

		else:
			print("33333333333333333333333333333333333333")
			messages.warning(request, "Sorry, Invalid Login Details")
			return HttpResponseRedirect(reverse("main:sign_in"))

	else:
		context = {}
		return render(request, "main/sign_in.html", context )




def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)
		email = request.POST.get("username")
		password1 = request.POST.get("password1")
		password2 = request.POST.get("password2")

		app_users = AppUser.objects.filter(user__username=request.POST.get("username"))

		if request.POST.get("password2") != request.POST.get("password1"):
			messages.warning(request, "Make sure both passwords match")
			print("passwords didn't match")
			return HttpResponseRedirect(reverse("main:sign_up"))

		elif len(app_users) > 0:
			messages.warning(request, "Email Address already taken, try another one!")
			print("email address already taken")
			return HttpResponseRedirect(reverse("main:sign_up"))
			
		else:
			user = form.save()
			user.set_password(request.POST.get("password1"))
			user.save()

			app_user = AppUser.objects.create(user=user)
			app_user.save()

			user = app_user.user
			user.email = email
			user.save()

			wallet = requests.post("http://127.0.0.1:4000/create-wallet/", data={"username": app_user.user.username}).json()
			wallet_address = wallet["public_key"]
			wallet_key = wallet["private_key"]

			app_user.wallet_address = wallet_address
			app_user.wallet_key = wallet_key
			app_user.save()

			if user:
				if user.is_active:
					login(request, user)

					app_user = AppUser.objects.get(user__pk=request.user.id)

					if app_user.user.username == "admin@iotexchartapp.com":
						print("11111111111111111111111111111111")
						messages.success(request, "Welcome Onboard Admin!")
						return HttpResponseRedirect(reverse("admin_app:index"))

					else:
						messages.warning(request, "Welcome Onboard")
						print("welcome Onboard")
						return HttpResponseRedirect(reverse("app:index"))

	else:
		form = UserForm()
		context = {"form": form}
		return render(request, "main/sign_up.html", context )

