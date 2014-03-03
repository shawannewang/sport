from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(unique=True, max_length=50)
	number = models.CharField(unique=True, max_length=12)
	year = models.CharField(unique=False, max_length=10)
	position = models.CharField(unique=False, max_length=20)
	height = models.TextField(unique=False, max_length=3)
	kill = models.TextField(unique=False)
	attack = models.TextField(unique=False)
	block = models.TextField(unique=False)
	dig = models.TextField(unique=False)
	personal = models.TextField(unique=False)
	imageurl = models.TextField(unique=False, null=True)

	class Meta(object):
		verbose_name_plural = 'Members'
		ordering = ('name', 'number', 'year', 'height', 'position', 'kill', 'attack', 'block', 'dig', 'personal')

	def __unicode__(self):
		return U'%s %s %s %s %s %s %s %s %s %s' %(self.name, self.number, self.year, self.height, self.position, self.kill, self.attack, self.block, self.dig, self.personal)

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
