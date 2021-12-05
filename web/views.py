from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
import json
from .models import CycleService
from .forms import CycleServiceForm,ShuttleServiceForm,FitnessServiceBranchForm,FitnessServiceOnsiteForm


def index(request):
    context = {
        "is_index" : True
    }
    return render(request, 'index.html',context) 


def service(request):
    context = {
        "is_service" : True
    }
    return render(request, 'service.html',context)

def cycleservice(request):
    form = CycleServiceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Get Back You Soon!"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_cycleservice" : True,
            "form":form
        }
    return render(request, 'cycleservice.html',context)

def shuttleservice(request):
    form = ShuttleServiceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Get Back You Soon!"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_shuttleservice" : True,
            "form":form
        }
    return render(request, 'shuttleservice.html',context)

def fitnessServiceBranch(request):
    form = FitnessServiceBranchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Get Back You Soon!"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_fitnessServiceBranch" : True,
            "form":form
        }
    return render(request, 'fitnessServiceBranch.html',context)


def fitnessServiceOnsite(request):
    form = FitnessServiceOnsiteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Get Back You Soon!"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "title" : "Form validation error",
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        context = {
            "is_fitnessServiceOnsite" : True,
            "form":form
        }
    return render(request, 'fitnessServiceOnsite.html',context)
