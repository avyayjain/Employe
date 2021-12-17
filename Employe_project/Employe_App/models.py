from django.db import models

# Create your models here.




class Position(models.Model):
    pos_tite = models.CharField(max_length=10)
    
    def __str__(self):
        return self.pos_tite



class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=  True)
    emp_name = models.CharField(max_length= 20)
    emp_mobile_no = models.IntegerField()
    emp_email = models.EmailField()
    emp_address = models.TextField(max_length=100)
    emp_dob = models.DateField(null=True)
    emp_pic= models.ImageField(upload_to = 'pics',null = True)
    pos = models.ForeignKey(Position,on_delete=models.CASCADE,null=True)


    
