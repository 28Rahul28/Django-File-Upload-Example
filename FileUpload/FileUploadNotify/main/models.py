from django.db import models
import os
from model_utils import FieldTracker
# Create your models here.


class FileData(models.Model):
    encrypted_data = models.CharField(max_length=264)
    UploadedFile = models.FileField(upload_to='', )
    tracker = FieldTracker(fields=['UploadedFile'])
    def __str__(self):
        return os.path.basename(self.UploadedFile.name)