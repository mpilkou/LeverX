from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
# base.User
# AbstractUser
class Teacher(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

class Student(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #class Meta:
    #    permissions = [
    #        ("student", "student permisions"),
    #    ]

class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)

class Lection(models.Model):

    title = models.CharField(max_length=80, blank=False)
    presentation = models.TextField(blank=False)


    course = models.ForeignKey(Course, on_delete = models.PROTECT)

class Homework(models.Model):
    txt = models.CharField(max_length=200, blank=False)
    comment = models.CharField(max_length=40, blank=True)
    mark = models.DecimalField(max_digits=3, decimal_places=0, blank=True)

    lection = models.ForeignKey(Lection, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
