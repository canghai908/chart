from django.db import models

# Create your models here.
class health(models.Model):
    host = models.CharField(max_length=30)
    def __unicode__(self):
    	return self.host

