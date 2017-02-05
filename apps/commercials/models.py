from __future__ import unicode_literals

from django.db import models
from ..users.models import User
# Create your models here.





class Commercial(models.Model):
	title = models.CharField(max_length=45, default="")
	company = models.CharField(max_length=45, default="")
	youtube = models.CharField(max_length=100, default="")
	
	FUNNY = 'Fy'
	SERIOUS = 'Ss'
	SEXY = 'Sx'
	CUTE = 'Ct'
	CAMEO = 'Cm'
	NOSTALGIC = 'Nc'
	CATEGORY_CHOICES = (
		(FUNNY, 'Funny'),
		(SERIOUS, 'Serious'),
		(SEXY, 'Sexy'),
		(CUTE, 'Cute'),
		(CAMEO, 'Cameo'),
		(NOSTALGIC, 'Nostalgic'),
	)
	category = models.CharField(
		max_length=2,
		choices=CATEGORY_CHOICES,
		default=FUNNY,
	)

	ETHOS = 'E'
	PATHOS = 'P'
	LOGOS = 'L'
	KAIROS = 'K'
	TOPOS = 'T'
	RHETORIC_CHOICES=(
		(ETHOS, 'Ethos'),
		(PATHOS, 'Pathos'),
		(LOGOS, 'Logos'),
		(KAIROS, 'Kairos'),
		(TOPOS, 'Topos'),
	)
	rhetoric = models.CharField(
		max_length=1,
		choices=RHETORIC_CHOICES,
		default=PATHOS,
	)

	YES = 'Y'
	NO = 'N'
	EFFICACY_CHOICES=(
		(YES, 'Yes'),
		(NO, 'No'),
	)
	efficacy = models.CharField(
		max_length=1,
		choices=EFFICACY_CHOICES,
		default=YES,
	)

	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)








class Vote(models.Model):
	user = models.ForeignKey(User)
	commercial = models.ForeignKey(Commercial, related_name="votes")


class Adpost(models.Model):
	content = models.TextField(max_length=250, default="")
	user = models.ForeignKey(User)
	commercial = models.ForeignKey(Commercial)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



	# get_FOO_display()

	# # -title
 #  -category (learn selecting multiple choices)
 # 	(can I load clips?)
	# funny, sexy, cute, serious, cameo, nostalgic, continuation(film/tv)
 #  -rhetoric
	# Ethos(credibility), Pathos(emotion), Logos, Kairos(timing), Topos(metaphor)
 #  -efficacy
 #  -industry
	# retail, automotive, telecom, financial, restaurants, insurance, pharmaceutical, food, travel/tourism, non-RX remedies 

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