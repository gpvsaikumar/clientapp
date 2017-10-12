# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import urllib2
import json

# Create your views here.
def read(request):
	
	req=urllib2.Request("http://10.0.3.23:8000/clapp/household/")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l=json.loads(f.read())
	k=[]

	return HttpResponse(l)
		
def index(request):
	return render(request,'clapp/index.html')


def create(request):
	name=request.POST['name']
	gender=request.POST['gender']
	age=request.POST['age']
	obj=Household(name=name,gender=gender,age=age)
	obj.save()
	return HttpResponseRedirect(reverse('clapp:index'))

def signup(request):
	return render(request, 'clapp/signup.html')


def test3(request):

	req=urllib2.Request("http://10.0.3.23:9456/task3app/household")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l=json.loads(f.read())
	j1_lat=[]
	j1_lng=[]
	j1_in=[]
	j2=[]
	j3=[]
	j3_name=[]
	j4_lat=[]
	j4_long=[]
	j5=[]
	j6_lat=[]
	j6_lng=[]
	j6_depth=[]
	j7_image=[]

#print 'Name:',l[0]['name']
	for i in l:
		
		j1_lat.append(i['latitude'])
		j1_lng.append(i['longitude'])
		j1_in.append(i['income'])
		
		
	req=urllib2.Request("http://10.0.3.23:9456/task3app/point")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l1=json.loads(f.read())

	req=urllib2.Request("http://10.0.3.23:9456/task3app/farm")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l2=json.loads(f.read())

	req=urllib2.Request("http://10.0.3.23:9456/task3app/member")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l3=json.loads(f.read())

	req=urllib2.Request("http://10.0.3.23:9456/task3app/photo")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l4=json.loads(f.read())

	req=urllib2.Request("http://10.0.3.23:9456/task3app/well")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l5=json.loads(f.read())

	req=urllib2.Request("http://10.0.3.23:9456/task3app/crop")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l6=json.loads(f.read())

	req=urllib2.Request("http://10.0.3.23:9456/task3app/cropping")
	opener=urllib2.build_opener()
	f=opener.open(req)
	l7=json.loads(f.read())


	for k in l2:
		j2.append(k['area'])

	for i in l:
		count=0
		for m in l3:
			if m['H_id']==i['id']:
				count+=1
				name=m['name']
		j3.append(count)
		j3_name.append(str(name))
		


	for i in l:
		for n in l4:
			if n['H_id']==i['id']:
				o=n['url']
		
		j5.append(str(o))	

	
	for i in l2:
		p=[]	
		o=[]
		for j in l1:
			if j['F_id'] == i['id']:
				p.append(j['P_lat'])
				o.append(j['P_long'])
		j4_lat.append(p)
		j4_long.append(o)

	for a in l5:
		j6_lat.append(a['w_lat'])
		j6_lng.append(a['w_long'])
		j6_depth.append(a['well_water_depth'])
	

	
	context={'j1_lat':j1_lat,'j1_lng':j1_lng,'j1_in':j1_in,'j2':j2,'j3':j3,'j3_name':j3_name,'j4_lat':j4_lat,'j4_long':j4_long,'j5':j5,'j6_lat':j6_lat,'j6_lng':j6_lng,'j6_depth':j6_depth,'l4':l4}



	return render(request, 'clapp/test3.html',context)
