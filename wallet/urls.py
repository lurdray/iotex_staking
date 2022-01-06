from django.urls import path
from . import views

app_name = "wallet"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("send-1/", views.Send1View, name="send1"),
	path("send-2/", views.Send2View, name="send2"),
	
	path("receive/", views.ReceiveView, name="receive"),

]

