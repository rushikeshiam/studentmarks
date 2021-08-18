from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    RollNo=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=40)
    Class=models.CharField(max_length=40)
    School=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    Address=models.CharField(max_length=240)

    class Meta:
        db_table="StudentInfo"


class StudentAcademics(models.Model):
    RollNo=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Biology=models.IntegerField()
    English=models.IntegerField()

    class Meta:
        db_table="StudentAcademics"
