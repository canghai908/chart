from django.db import models

# Create your models here.
class health(models.Model):
    host = models.CharField(max_length=30)
    ping = models.IntegerField(max_length=30)
    date = IntegerField
    traffic_in = models.FloatField(max_digits=19,decimal_places=10)
    traffic_out = models.FloatField(max_digits=19,decimal_places=10)
    def __unicode__(self):
    	return self.host
class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	def __unicode__(self):
		return self.username
