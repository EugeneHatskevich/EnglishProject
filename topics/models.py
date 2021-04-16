from django.db import models

# Create your models here.
class Topics(models.Model):
    topic_id = models.CharField(max_length=255)