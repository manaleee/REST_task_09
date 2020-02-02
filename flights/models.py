from django.db import models
from django.contrib.auth.models import User


# ----------  signals -----------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver 





#------------------------------------------------------------------
class Flight(models.Model):
	destination = models.CharField(max_length=100)
	time = models.TimeField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	miles = models.PositiveIntegerField()

	def __str__(self):
		return "to %s at %s" % (self.destination, str(self.time))




#----------------------------------------------------------------------------------------
class Booking(models.Model):
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="bookings")
	date = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="bookings")
	passengers = models.PositiveIntegerField()

	def __str__(self):
		return "%s: %s" % (self.user.username, str(self.flight))




# ---------------------- signale ADD booking ------------------------------
@receiver(post_save, sender=User)
def create_profile(instance, *args, **kwargs):
    Profile.objects.create(user = instance )


   




#----------------------------------------------
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	miles = models.PositiveIntegerField(default=0)

	def __str__(self):
		return str(self.user)




# ---------------------- signale CREATE profile ------------------------------
@receiver(post_save, sender=Booking)
def create_profile(instance, *args, **kwargs):
    Profile.objects.create(user = instance )






# # ---------------------- signale CANCELLED profile ------------------------------
@receiver(post_save, sender=User)
def cancell_profile(instance, *args, **kwargs):
    Profile.objects.cancel(user = instance )    



