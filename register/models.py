from django.db import models


class Register(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    ROLE_CHOICES = (
        (u'SE', u'SOFTWARE ENG'),
        (u'TL', u'TEAM LEAD'),
        (u'SSE', u'SNR.SOFTWARE ENG'),
        (u'CEO', u'CEO'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    exp = models.IntegerField()
    salary = models.FloatField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateTimeField()
    role = models.CharField(max_length=4, choices=ROLE_CHOICES)
    active = models.BooleanField()

    class Meta:
        db_table = 'REGISTER_INFO'



