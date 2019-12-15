from django.db import models
import os
# Create your models here.


class FileData(models.Model):
    encrypted_data = models.CharField(max_length=264)
    UploadedFile = models.FileField(upload_to='', )
    def __str__(self):
        return os.path.basename(self.UploadedFile.name)
