from django.shortcuts import render
from .models import Job , Categories
from django.core.paginator import Paginator
# Create your views here.


def job_list(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 3) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"data" : page_obj}
    print(jobs)
    return render(request , 'job/job_list.html' , context)


def job_detals(request , id):
    job_details = Job.objects.get(id=id)
    context = {"data" : job_details}
    return render(request , 'job/job_details.html' , context)