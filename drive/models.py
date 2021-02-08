from django.db import models


class AyenDrive(models.Model):
    title = models.CharField(max_length=128, null=False)
    file = models.FileField(upload_to='file/')