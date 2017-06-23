from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.document)

class uploadedFiles(models.Model):
    name = models.CharField(max_length = 60)
    file_store = models.FileField(upload_to = 'files_stored')
    class Meta:
        db_table = "uploadedFiles"
    def __str__(self):
        return str(self.name)

class Document_classification(models.Model):
    virusTotal_rate = models.CharField(max_length = 255, null=True)
    deepAnalyser_rate = models.CharField(max_length = 255, null = True)
    document = models.ForeignKey(Document, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.document)

class Document_fingerPrints(models.Model):
    sha1 = models.CharField(max_length = 255, null = True)
    sha256 = models.CharField(max_length = 255, null = True)
    md5 = models.CharField(max_length = 255, null = True)
    document = models.ForeignKey(Document, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.sha256)