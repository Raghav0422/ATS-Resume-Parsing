from django import forms
from .models import PDFDocumentModel

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocumentModel
        fields = ['name', 'file']  # We hide 'extracted_text' because the user shouldn't type it manually