from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("sign-up/", views.SignUpView, name="sign_up"),
	path("sign-in/", views.SignInView, name="sign_in"),


]

