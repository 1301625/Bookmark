from django.db import models


# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField("Site URL")

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # 모델 정렬 지정하기
    class Meta:
        ordering = ['-id']
