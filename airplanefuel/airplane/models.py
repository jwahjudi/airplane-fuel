import datetime

from django.db import models

class Airplane(models.Model):
	passengers = models.IntegerField(default=-1)

	def count_fuel_tank(self):
		return self.id * 200
	fuel_tank = property(count_fuel_tank)

	def count_consumption_per_min(self):
		return (self.id * 0.8) + (self.passengers * 0.002)
	consumption_per_min = property(count_consumption_per_min)

	def max_flying_time(self):
		return (self.id * 200)/((self.id * 0.8) + (self.passengers * 0.002))
	max_flying_time = property(max_flying_time)

	def __str__(self):
		return str(self.id)