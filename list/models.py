from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=30)
    Email=models.EmailField()
    phone_number=models.IntegerField()
    Designation=models.CharField(max_length=20)
    company_name=models.CharField(max_length=10)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.firstname