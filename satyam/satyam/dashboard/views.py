from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Track, Service, Costumer, Document

class ServiceDetail(DetailView):
    model = Service

def index(request):
    detail= Service.objects.all().filter(category='notification')
    service= Service.objects.all().filter(category='student')
    serv= Service.objects.all().filter(category='common')
    ser= Service.objects.all().filter(category='business')
    se= Service.objects.all().filter(category='govtscheme')
    s= Service.objects.all().filter(category='digital')
    ot= Service.objects.all().filter(category='other')
    
    context={'ot':ot,'service': service, 'service1': ser, 'service2': serv,'service3':se, 'service4':s, 'detail': detail}
    return render(request, 'dashboard/index.html', context)

def track(request):
    name = request.GET.get('name')
    tray = Track.objects.filter(trackid=name)
    print(tray)
    param = {'tracks': tray, 'msg': ""}
    if len(tray) == 0 or len(name) <0:
        param = {'msg': "make sure not enter text only number"}
    return render(request, 'dashboard/track.html', param)


def search(request):
    que= request.GET.get('search')
    context = Service.objects.all().filter(name__icontains=que)
    params = {'service':context, 'msg':""}
    if len(context) ==0 or len(que) ==0:
        params = {'msg':"Please make sure to enter relevent search"}
    return render(request, 'dashboard/search.html', params)

class ServiceCreateView(SuccessMessageMixin, CreateView):
    model = Service
    fields = ['category','name', 'discription']
    success_url = '/'
    success_message = "Message Send was successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DocumentCreateView(SuccessMessageMixin, CreateView):
    model = Document
    fields = ['service_name','document']
    success_url = '/'
    success_message = "Message Send was successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CostumerCreateView(SuccessMessageMixin, CreateView):
    model = Costumer
    fields = ['name','email', 'phone', 'message','choose_service','service_document', 'document']
    success_url = '/track'
    success_message = "Message Send was successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


