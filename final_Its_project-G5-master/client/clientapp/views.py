# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
#from .models import Kissan
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import requests
import json
import urllib
from django.http import HttpResponseRedirect
from .forms import NameForm
from .forms import MailForm
#from django.utils import simplejson
# Create your views here.
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

url = 'http://127.0.0.1:1996/kissans'
response = urllib.urlopen(url)
kissans =json.loads(response.read())

url1 = 'http://127.0.0.1:1996/farms'
response1 = urllib.urlopen(url1)
dat2 = json.loads(response1.read())

url2 = 'http://127.0.0.1:1996/wells'
response2 = urllib.urlopen(url2)
data = json.loads(response2.read())

url3 = 'http://127.0.0.1:1996/houses'
response3 = urllib.urlopen(url3)
dat1 = json.loads(response3.read())

url4 = 'http://127.0.0.1:1996/familymembers'
response4 = urllib.urlopen(url4)
dat3 = json.loads(response4.read())

url5 = 'http://127.0.0.1:1996/cropprices'
response5 = urllib.urlopen(url5)
dat5 = json.loads(response5.read())

url6 = 'http://127.0.0.1:1996/fertilizers'
response6 = urllib.urlopen(url6)
dat6 = json.loads(response6.read())


def rend(request):
    return render(request,'clientapp/apple.html',context={'data':data,'dat1':dat1, 'dat2':dat2 } )

def crop(request):
    return render(request,'clientapp/cropprices.html',context={'dat5':dat5 })

def fertilizer(request):
    return render(request,'clientapp/fertilizers.html',context={'dat6':dat6 })


def rend1(request):
    return render(request,'clientapp/applw.html',context={'data':data,'dat1':dat1, 'dat2':dat2 } )
data2=[]
data1=[]
data3=[]
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
		P=form.cleaned_data['Phone']
		Pw=form.cleaned_data['Pwd']
		form = NameForm()
		for k in kissans:
			if str(k['Phone'])==P and k['Password']==Pw:
				request.session['K_id'] = k['id']
    				for d in dat2:
					if d['F_id']==request.session['K_id']:
						data2.append(d)
				for d in dat1:
					if d['F_id']==request.session['K_id']:
						data1.append(d)
				for d in dat3:
					if d['F_id']==request.session['K_id']:
						data3.append(d)
		                return render(request,'clientapp/alogin.html',context={'data':data,'data1':data1, 'data2':data2,'k':k,'data3':data3 } )	
    else:
        form = NameForm()

    return render(request, 'clientapp/contacts.html', {'form': form})

def map(request):
	return render(request,'clientapp/maps.html',context={'data':data,'data1':data1, 'data2':data2,'data3':data3 } )

def home(request):
	return render(request,'clientapp/index.html')

def mail(request):
	form = MailForm(request.POST)
        if form.is_valid():
		P=form.cleaned_data['msg']
		msg = MIMEMultipart()
		msg['From'] = 'santosh.velamala@gmail.com'
		msg['To'] = 'santhosh.v15@iiits.in'
		msg['Subject'] = 'Advice for my crop'
		message = 'here is the email'
		msg.attach(MIMEText(P))
		mailserver = smtplib.SMTP('smtp.gmail.com',587)
		mailserver.ehlo()
		mailserver.starttls()
		mailserver.ehlo()
		mailserver.login('santosh.velamala@gmail.com', '9440206496')
		mailserver.sendmail('santosh.velamala@gmail.com','santhosh.v15@iiits.in',msg.as_string())
		mailserver.quit()
	else:
        	form = MailForm()
	return render(request, 'clientapp/mail.html', {'form': form})

