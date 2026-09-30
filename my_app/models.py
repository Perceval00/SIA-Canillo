from django.db import models

class Student(models.Model):
    student = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    room = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.student_id