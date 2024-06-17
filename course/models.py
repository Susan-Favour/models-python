from django.db import models

# Create your models here.

class Teacher(models.Model):
    id_number = models.IntegerField
    course_name = models.CharField(max_length=20)
    course_department = models.CharField(max_length=25)
    enrollment_limit = models.IntegerField()
    trimester = models.PositiveSmallIntegerField()
    course_description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
