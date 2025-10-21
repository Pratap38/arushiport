from django.db import models

class ProfilePic(models.Model):
    image = models.ImageField(upload_to='profile_pics/')

class Project(models.Model):
    tittle=models.CharField(max_length=50)
    describe=models.TextField()
    image=models.ImageField(upload_to='project_image/')
    Project_link=models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.tittle
class Contact(models.Model):
    full_name=models.CharField()
    email=models.EmailField()
    phone=models.CharField(max_length=15,blank=True)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str____(self):
        return f"Message from {self.full_name}"