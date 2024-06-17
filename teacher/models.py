from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    course_id = models.IntegerField()
    country = models.CharField(max_length=28)
    education_level = models.CharField(max_length=35)
    id_number = models.IntegerField()
    subject_specialisation = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    

