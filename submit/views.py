from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm

# Create your views here.

def upload(request):
    return render(request, 'submit/upload.html')

def home(request):
    documents = Document.objects.all()
    return render(request, 'submit/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'submit/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'submit/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'submit/model_form_upload.html', {
        'form': form
    })