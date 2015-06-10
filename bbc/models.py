from django.db import models

class Biobank(models.Model):
    name = models.TextField(default='')
    pass

class Study(models.Model):
    name = models.TextField(default='')
    biobank = models.ForeignKey(Biobank, default=None)

