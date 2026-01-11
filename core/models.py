from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(
        max_length = 15,
        null = True,
        blank = True
    )
    is_active = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)