from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import JobApplication
from .forms import JobApplicationForm
from django.db.models import Count

def home(request):
    total = JobApplication.objects.count()
    status_counts = JobApplication.objects.values('status').annotate(count=Count('status'))
    status_dict = {item['status']: item['count'] for item in status_counts}
    context = {
        'total': total,
        'status_counts': status_dict,
    }
    return render(request, 'home.html', context)

def job_list(request):
    jobs = JobApplication.objects.all().order_by('-application_date')
    return render(request, 'jobs/list.html', {'jobs': jobs})

def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application added successfully!')
            return redirect('jobs:job_list')          
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/create.html', {'form': form})

def job_detail(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    return render(request, 'jobs/detail.html', {'job': job})

def job_update(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application updated successfully!')
            return redirect('jobs:job_list')          
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'jobs/update.html', {'form': form, 'job': job})

def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Application deleted successfully!')
        return redirect('jobs:job_list')              
    return render(request, 'jobs/delete.html', {'job': job})