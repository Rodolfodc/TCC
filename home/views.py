from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home/index.html')

#def submit_file(request):
#    return HttpResponse("Esta pagina eh para submeter arquivos")