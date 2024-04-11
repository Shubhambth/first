from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Service(models.Model):
    post_title=models.CharField(max_length=100)
    post_description=HTMLField()
    post_image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)

    news_slug=AutoSlugField(populate_from='post_title',unique=True,null=True,default=None)






# Create your models here.
