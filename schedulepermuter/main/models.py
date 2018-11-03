from django.db import models

# Create your models here.

class ScheduleOwner(models.Model):
	pass

class Institution(models.Model):
	name = models.CharField(max_length=64)
	code = models.CharField(max_length=8)

class Department(models.Model):
	institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	code = models.CharField(max_length=16)

class Course(models.Model):
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	number = models.CharField(max_length=8)
	title = models.CharField(max_length=32)

class Professor(models.Model):
	name = models.CharField(max_length=64)
	institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

class Section(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	uid = models.CharField(max_length=16)
	TYPES = (
		('M', 'Main'),
		('A', 'Additional'))
	section_type = models.CharField(max_length=1, choices=TYPES)
	monday = models.BooleanField(default=False)
	tuesday = models.BooleanField(default=False)
	wednesday = models.BooleanField(default=False)
	thursday = models.BooleanField(default=False)
	friday = models.BooleanField(default=False)
	start_time = models.TimeField()
	end_time = models.TimeField()
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE)