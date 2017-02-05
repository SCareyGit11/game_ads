from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.



class UserManager(models.Manager):

	def login(self, username, password):
		errors = []
		print 50*'All'
		for user in User.objects.all():
			print user.username
		
		### CHECK FOR FIELD ERRORS ###
		if len(username) < 2 or len(password) < 8:
			errors.append('login')
			return {'errors':errors}

		elif User.objects.filter(username=username):
			user = User.objects.filter(username=username)[0]
			hashed = user.password
			### IF LOGIN PASSWORD HASHED MATCHES USER'S HASHED PASSWORD ###
			if hashed == bcrypt.hashpw(password.encode(), hashed.encode()):
				return {'member':user}
			else:
				errors.append('login')
				return {'errors':errors}	

		else:
			errors.append('login')
			return {'errors':errors}



	def register(self, username, password):
		### Make an empty list 'errors' to fill with key/value pairs and pass back to the controller ###
		errors = []

		### IF USER HAS ALREADY REGISTERED ###
		try:
			user = User.objects.get(username=username)
			errors.append('exists')
			return {'errors':errors}
		except: 
			#### ALL FIELDS MUST BE COMPLETED ###
			if len(username) < 1 or len(password) < 1:
				
				errors.append('field')
				print errors

			### CHECK FOR FIELD SPECIFIC ERRORS ###
			if len(username) < 2:
				errors.append('username') 
				print errors
			


			if len(password) < 8:
				errors.append('password')

			

			if len(errors) > 0:
				return {'errors':errors}
			### IF NO ERRORS, HASH THE PW AND CREATE NEW USER ###
			
			else:
				hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
				user = User.objects.create(username=username, password=hashed, status='G')
				return {'newuser':user}

class User(models.Model):
	
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=255)
	ADMIN = 'A'
	GUEST = 'G'
	STATUS_CHOICES = (
		(ADMIN, 'Admin'),
		(GUEST, 'Guest')
	)
	status = models.CharField(
		max_length=1,
		choices=STATUS_CHOICES,
		default=GUEST
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	# class Student(models.Model):
 #    FRESHMAN = 'FR'
 #    SOPHOMORE = 'SO'
 #    JUNIOR = 'JR'
 #    SENIOR = 'SR'
 #    YEAR_IN_SCHOOL_CHOICES = (
 #        (FRESHMAN, 'Freshman'),
 #        (SOPHOMORE, 'Sophomore'),
 #        (JUNIOR, 'Junior'),
 #        (SENIOR, 'Senior'),
 #    )
 #    year_in_school = models.CharField(
 #        max_length=2,
 #        choices=YEAR_IN_SCHOOL_CHOICES,
 #        default=FRESHMAN,
 #    )

 #    def is_upperclass(self):
 #        return self.year_in_school in (self.JUNIOR, self.SENIOR)
