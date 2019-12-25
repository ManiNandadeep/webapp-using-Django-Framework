#Django includes a 'Signal Dispatcher' which will notify when an event/action has occurred
#some useful notifications are django.db.models.signals.pre_save &django.db.models.post_save sent before and after save() method is called
from django.db.models.signals import post_save
#here User is the sender
from django.contrib.auth.models import User
#importing receiver from django.dispatch
from django.dispatch import receiver
from .models import Profile

# method for creating a profile
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
		if created:
			Profile.objects.create(user=instance)

# method for saving a profile
@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
		instance.profile.save()
