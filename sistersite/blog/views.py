from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UploadedFile
from .forms import UploadFileForm
from .paginator_views import paginator

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    page_obj = paginator(request, files)
    return render(request, 'upload_file.html', {'form': form, 'files': files, 'page_obj': page_obj,})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def post_detail(request, year, month, day):
    file = get_object_or_404 (UploadedFile, 
            publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'detail.html', {'file': file })
