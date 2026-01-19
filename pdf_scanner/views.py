import fitz  # This is PyMuPDF
from django.shortcuts import render, redirect

from .forms import PDFUploadForm

from .models import PDFDocumentModel

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def dashboard_view(request):
    query = request.GET.get('q')
    
    # Logic for Uploading
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_instance = form.save(commit=False)
            # PyMuPDF extraction
            file_bytes = request.FILES['file'].read()
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            pdf_instance.extracted_text = "".join([page.get_text() for page in doc])
            pdf_instance.save()
            return redirect('dashboard')

    # Logic for Searching & Listing
    pdfs = PDFDocumentModel.objects.all().order_by('-upload_date')
    if query:
        pdfs = pdfs.filter(extracted_text__icontains=query)

    return render(request, 'pdf_scanner/dashboard.html', {
        'form': PDFUploadForm(),
        'pdfs': pdfs,
        'query': query
    })