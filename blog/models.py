from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class Study(models.Model):
    title=models.CharField(max_length=15)
    subject=models.CharField(max_length=15)
    content=models.TextField(max_length=1000)
    level=models.PositiveSmallIntegerField(validators=[MaxValueValidator(6)])
    importance=models.PositiveSmallIntegerField(validators=[MaxValueValidator(6)])
    repeat=models.PositiveSmallIntegerField()
    created_at=models.DateField(auto_now_add=True)
    modified_at=models.DateField(auto_now=False,blank=True)
    def get_absolute_url(self):
        return reverse('blog:study-detail',args=self.pk)


class Reference(models.Model):
    title = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    address = models.URLField()
    created_at = models.DateField(auto_now_add=True)

class Memo(models.Model):
    title=models.CharField(max_length=10)
    content = models.TextField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)