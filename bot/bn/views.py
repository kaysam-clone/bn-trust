from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
from django.core import serializers
from django.http import response


def donna_users(request):
    users = DonnaUsers.objects.all()
    x = ['user']
    y='samson111'
    for i in users:
        x.append(f'{i}')
    print(x)
    response = {}
    response= serializers.serialize("json", DonnaUsers.objects.all())
    return HttpResponse(response)

def mohammed_users(request):
    users = MohammedUsers.objects.all()
    x = ['user']
    y='samson111'
    for i in users:
        x.append(f'{i}')
    print(x)
    response = {}
    response= serializers.serialize("json", MohammedUsers.objects.all())
    return HttpResponse(response)



def guest_users(request):
    users = GuestUsers.objects.all()
    x = ['user']
    y='samson111'
    for i in users:
        x.append(f'{i}')
    print(x)
    response = {}
    response= serializers.serialize("json", GuestUsers.objects.all())
    return HttpResponse(response)

def create_d(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        DonnaUsers.objects.create(username = username)

    return render(request, 'create_d.html')

def create_m(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        MohammedUsers.objects.create(username = username)

    return render(request, 'create_m.html')

def create_g(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        GuestUsers.objects.create(username = username)

    return render(request, 'create_g.html')
