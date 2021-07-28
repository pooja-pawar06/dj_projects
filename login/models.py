from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    dob = models.DateTimeField()
    active = models.BooleanField()

    class Meta:
        db_table = 'STUDENT_INFO'       #__table_name__

