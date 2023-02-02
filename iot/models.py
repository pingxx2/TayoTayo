from django.db import models

# 녹화파일 업로드
class SecFile(models.Model):
    file_name = models.CharField(max_length=100)
    sec_file = models.FileField(upload_to="")
