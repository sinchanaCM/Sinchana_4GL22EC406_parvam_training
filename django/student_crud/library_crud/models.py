from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    usn = models.IntegerField()
    branch= models.CharField(max_length=20, unique=True)
    bookname = models.CharField(max_length=50)
    booknumber = models.CharField(max_length=50)
    authorname = models.CharField(max_length=50)
    subject = models.IntegerField()
    
    def __str__(self):
        return self.name