from django.urls import path
from . import views

app_name = "staking"

urlpatterns = [

	path("stake/", views.StakeView, name="stake"),
	path("my-stakes/", views.MyStakesView, name="my_stakes"),

]

