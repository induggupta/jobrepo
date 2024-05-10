from django.shortcuts import render
from testapps.models import HydJobs

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')
def HydJobs_view(request):
    job_list=HydJobs.objects.all()
    return render(request,'testapp/hyd.html',{'job_list':job_list})
def HydJobs_view(request):
    job_list=PuneJobs.objects.all()
    return render(request,'testapp/hyd.html',{'job_list':job_list})

def Jobs_view(request):
    job_list=HydJobs.objects.all()
    return render(request,'testapp/hyd.html',{'job_list':job_list})
