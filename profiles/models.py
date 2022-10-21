from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.IntegerField( null=True, blank=True)
    profile_image = models.ImageField(default=None, null=True, blank=True, upload_to='profile_pics')
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    