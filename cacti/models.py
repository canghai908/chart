from django.db import models

# Create your models here.
class health(models.Model):
    host = models.CharField(max_length=30)
    ping = models.IntegerField(max_length=30)
    def __unicode__(self):
    	return self.host
class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	def __unicode__(self):
		return self.username
