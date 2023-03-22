from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    salary=models.IntegerField()
