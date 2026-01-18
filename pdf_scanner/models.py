from django.db import models

# Create your models here.

class PDFDocumentModel(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(blank=True, null=True)  # To store text for faster searching

    def __str__(self):
        return self.name