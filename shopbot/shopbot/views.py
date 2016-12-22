from django.http import HttpResponse
from .models import ShopBot, ShopBotDatabase
import random
from django.shortcuts import render_to_response
from . import shopbot

def add_user(request):
	user = random.randint(100000,10000000)
	ShopBot.objects.create(userid=user)
	return HttpResponse("User Made: Now proceed to add product information")


def show_frame(request):
	userid = request.GET.get("userid")
	obj_user = None
	if userid:
		try:
			obj_user = ShopBot.objects.get(userid=userid)
			print obj_user
			obj = ShopBotDatabase.objects.filter(userid=obj_user)
			print obj
			data = []

			for i in obj:
				data.append(i.product_desc)


			data.append(shopbot.get_combined_text())

			return render_to_response("show.html",{"data":data,"userid":obj_user.userid})


		except:
			print 'Error: no such user'
			return HttpResponse("error")

	else:
		print "wrong"

def generate_url(request):
	l = []
	for i in ShopBot.objects.all():
		l.append(i.userid)

	return render_to_response("list.html",{'l':l})