import datetime

from django.db import models

class Airplane(models.Model):
	airplane_id = models.IntegerField(default=-1)
	passengers = models.IntegerField(default=-1)
	def __str__(self):
		return self.airplane_id
	def count_fuel_tank(self):
		return self.airplane_id * 200
	def count_consumption_per_min(self):
		return (self.airplane_id * 0.8) + (self.passengers * 0.002)

