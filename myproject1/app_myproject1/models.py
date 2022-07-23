from django.db import models

# Create your models here.
class Userdetails(models.Model):
    first_name= models.CharField(max_length=100)
    second_name= models.CharField(max_length=100, null=True)
    last_name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    is_verified=models.BooleanField(default=False)
    verfication_code=models.CharField(max_length=10, blank=True)
    class Meta:
        db_table="User_details"

class UserAcademic(models.Model):
    academic_level=models.CharField(max_length=50)
    org_name=models.CharField(max_length=100)
    board_name=models.CharField(max_length=50)
    start_year=models.DateField(default=0, null=True)
    end_year=models.DateField(default=0, null=True)
    total_rank=models.FloatField(max_length=5)
    rank=models.CharField(max_length=20)
    academic_certificate=models.FileField()
    academic_transcript=models.FileField()
    user=models.ForeignKey(Userdetails, on_delete=models.CASCADE, default=None)
    class Meta:
        db_table="User_Academic_details"

class workhistory(models.Model):
    org_name=models.CharField(max_length=100)
    org_locations=models.CharField(max_length=100)
    job_category=models.CharField(max_length=100)
    job_position=models.CharField(max_length=100)
    job_start=models.DateField()
    job_end=models.DateField(null=True, default=None)
    currently_working=models.BooleanField(null=True, default=False)
    user=models.ForeignKey(Userdetails, on_delete=models.CASCADE, default=None)


    class Meta:
        db_table="work_history"