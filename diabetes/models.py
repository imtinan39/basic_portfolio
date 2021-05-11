from django.db import models

from django.contrib.auth.models import User






class Info(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	
	created=models.DateTimeField(auto_now_add=True)
	insulin=models.FloatField()




	def __str__(self):


		return str(self.user)
	def datepublished(self):

	    return self.created.strftime('%d%m%Y')



class Pickle(models.Model):

	csv=models.FileField()




    