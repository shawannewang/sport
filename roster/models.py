from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(unique=True, max_length=50)
	number = models.CharField(unique=True, max_length=12)
	year = models.CharField(unique=False, max_length=10)
	position = models.CharField(unique=False, max_length=20)
	height = models.TextField(unique=False, max_length=3)
	imageurl = models.TextField(unique=False, null=True)

	class Meta(object):
		verbose_name_plural = 'Members'
		ordering = ('name', 'number', 'year', 'height', 'position')

	def __unicode__(self):
		return U'%s %s %s %s %s' %(self.name, self.number, self.year, self.height, self.position)

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Member, self).save(*args, **kwargs)

class Mentor(models.Model):
	name = models.CharField(unique=True, max_length=50)
	position = models.TextField(unique=False)

	class Meta(object):
		ordering = ('name', 'position')

	def __unicode__(self):
		return U'%s %s' %(self.name, self.position)
