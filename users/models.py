from django.db import models
from django.contrib.auth.models import User
from PIL import Image #importing the Image module from the PIL (python image library)



# A User will have a Profile and a Profile will be linked to only one user 
# so we will be using OneToOneField here
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)	
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'

	#overriding the save() method 
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img=Image.open(self.image.path)	

		if img.height>300 or img.width>300:		# if the size of the image is more than 300px then reduce the size of the image to speed up the webpage
			output_size=(300,300)				# output_size is a tuple of the reduced size of the image
			img.thumbnail(output_size)		#makes the image into a thumbnail which is no larger than the original image
		img.save(self.image.path)
			