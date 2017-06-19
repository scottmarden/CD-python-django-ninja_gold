# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random, datetime

locations = {
	'farm': [10,20],
	'cave': [5,10],
	'house': [2,5],
	'casino':[-50, 50]
}

# Create your views here.
def index(request):

	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activities' not in request.session:
		request.session['activities'] = []
	if 'class' not in request.session:
		request.session['class'] = []
	info = {
		'gold': request.session['gold'],
		'activities': request.session['activities'],
	}
	return render(request, 'ninja_app/index.html', info)

def process_gold(request):
	if request.method == 'POST':
		if request.POST['location'] == 'farm':
			#generate 10-20 gold
			new_gold = random.randint(10,20)
			request.session['gold'] += new_gold
			action = "Earned " + str(new_gold) + " gold from the farm! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		elif request.POST['location'] == 'cave':
			#generate 10-20 gold
			new_gold = random.randint(5,10)
			request.session['gold'] += new_gold
			action = "Earned " + str(new_gold) + " gold from the cave! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		elif request.POST['location'] == 'house':
			#generate 10-20 gold
			new_gold = random.randint(2,5)
			request.session['gold'] += new_gold
			action = "Earned " + str(new_gold) + " gold from the House! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		elif request.POST['location'] == 'casino':
			#generate 10-20 gold
			print "Went to the casino!"
			new_gold = random.randint(-50,50)
			request.session['gold'] += new_gold
			if new_gold < 0:
				action = "Entered a Casino and lost " +  str(new_gold) + " gold .... Ouch. " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			else:
				action = "Entered a Casino and won " + str(new_gold) + " gold... Nice! " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print action
		request.session['activities'].insert(0, action)

	return redirect('/')

def reset(request):
	if request.method == "POST":
		del request.session['gold']
		del request.session['activities']
	return redirect('/')
