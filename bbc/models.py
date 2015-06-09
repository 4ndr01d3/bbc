from django.db import models

class Study(models.Model):
    name = models.TextField(default='')
