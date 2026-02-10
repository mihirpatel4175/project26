from django.db import models

# Create your models here.
class student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=100)
    studentEmail = models.EmailField(null=True)
    
    class Meta:
        db_table = "student"
    def __str__(self):
        return self.studentName

class product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.IntegerField(null=True)
    productColor = models.CharField(max_length=100,null=True)
    productStatus = models.CharField(default=True)
    
    class Meta:
        db_table = "product"
    def __str__(self):
        return self.productName

class Branch(models.Model):
    branchName = models.CharField(max_length=100)
    branchSubject = models.CharField(max_length=100)
    branchCredit = models.IntegerField()
    branchCourseDuration = models.IntegerField()
    branchCourseFee = models.IntegerField()
    
    class Meta:
        db_table = "branch"
    def __str__(self):
        return self.branchName