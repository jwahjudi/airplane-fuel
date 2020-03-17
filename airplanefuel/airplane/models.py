import datetime

from django.db import models

class Airplane(models.Model):
	airplane_id = models.IntegerField(default=1)
	fuel_tank = airplane_id * 200
	passengers = models.IntegerField(default=0)
	consumption_per_min = (airplane_id * 0.8) + (passengers * 0.002)
	def __str__(self):
		return self.question_text

