from django.shortcuts import render, redirect, HttpResponse
import os, binascii
from django.contrib.auth import authenticate, login
from .models import *
from datetime import datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail


# Create your views here.
#booking page, showing booking page to users
def booking(request):
    template_name = "booking/booking.html"
    args = {}
    return render(request,template_name,args)


@csrf_exempt
def registrationapi(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    firstname = json_data['firstname']
    lastname = json_data['lastname']
    email = json_data['email']
    phone = json_data['phone']
    country = json_data['country']
    status = json_data['status']
    professionalstatus = json_data['professionalstatus']
    institution = json_data['institution']
    interest = json_data['interest']
    expectation =json_data['expectation']
    user = CustomUser()
    user.username = firstname
    user.first_name = firstname
    user.last_name = lastname
    user.email = email
    user.phone = phone
    user.country = country
    user.status = status
    user.professionalstatus = professionalstatus
    user.institution = institution
    user.interest = interest
    user.expectation =expectation
    user.save()
    msg = """Hello {}, You Have Succesfully Registered for our Leadership and Mentorship Masterclass.""".format(firstname)
    send_mail(
    'COME Leadership & Mentorship Masterclass',
    msg,
    'comecenters@gmail.com',
    [email],
    fail_silently=False,
    )
    data = {'success':True,'message':"Successfully Registered"}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')