from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Course(models.Model):
    Course_Name=models.CharField(max_length=40)

    def __str__(self):
        return f'{self.Course_Name}'

class Book(models.Model):
    Book_Name=models.CharField(max_length=40)
    Author_Name=models.CharField(max_length=40)
    Course_Id=ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Book_Name}'

class Student(models.Model):
    Stud_Name = models.CharField(max_length=50)
    Stud_Password = models.CharField(max_length=50)
    Stud_Phno = models.BigIntegerField()
    Stud_Semester=models.CharField(max_length=50)
    Stud_Course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Stud_Name}'

class IssueBook(models.Model):
    Student_Name=models.ForeignKey(Student,on_delete=models.CASCADE)
    Book_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    Start_Date=models.DateField()
    End_Date=models.DateField()


