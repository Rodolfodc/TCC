from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.conf import settings

from .forms import uploadForm, DocumentForm
from .models import uploadedFiles, Document, Document_classification, Document_fingerPrints
from . import virusTotal as vt
from . import file_misc

# def svUpload(request):
#     saved = False
#     print(">>>>>>>>>>>>TTTADDDAAAAAAAA<<<<<<<<<<<<")
#     if request.method == "POST":
#         upForm = uploadForm(request.POST, request.FILES)
#         print(">>>>>>>>>>Method is post")
#         if upForm.is_valid():
#             file_store = uploadedFiles()
#             file_store.name = upForm.cleaned_data["name"]
#             file_store.file_store = upForm.cleaned_data["file"]
#             file_store.save()
#             saved = True
#             print(">>>>>>>>>>>Form is valid")
#     else:
#         print(">>>>>>>>++++++ERROOUU")
#         upForm = uploadForm()
#         print(">>>>>>>IRINEEU<<<<NEM EU>><<>")
#         print("Method req:" + str(request.method))
#         print("upForm: "+ str(upForm))
#     render(request, 'teste_upload/teste_upload.html')

def model_form_upload(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            print("Documento Salvo!")
            filename = settings.MEDIA_ROOT+"/"+str(doc.document)
            print("**filename: "+filename)


            sha256_doc = file_misc.sha256_checksum(filename)
            json_response = vt.get_json_from_virusTotal(sha256_doc)

            if json_response['response_code'] == 0:
               	resource_code = vt.send_to_virusTotal(filename)
                print("resource_code: "+resource_code)
                vt_response_json = vt.get_json_from_virusTotal(resource_code)
            elif json_response['response_code'] == 1:
                vt_response_json = json_response

           
#            print(">>>>> vt_result: "+str(vt_response_json))
            doc_fp = Document_fingerPrints()
            print(">>>>> vt_sha256: "+sha256_doc)
            doc_fp.sha256 = sha256_doc
            doc_fp.md5 = vt_response_json['md5']

            doc_fp.document = doc

          #  doc_fp.save()

            vt_file_classification = vt_response_json['scans']['GData']['result']
            print(">>>>> vt_result: "+ str(vt_file_classification))

            doc_clas = Document_classification()
            doc_clas.virusTotal_rate = vt_file_classification
            doc_clas.document = doc
            doc_clas.save()

            print("Savou o doc_clas")

            return redirect("home:index")
    else:
        form = DocumentForm()
    return render(request, 'teste_upload/model_form_upload.html', {
        'form':form, 'documents':documents
    })
