from django.db import models


# Register your models here.
class API(models.Model):
    # apiKey generation is based on sha256, api_key = sha265(time+email)
    api_key = models.CharField(max_length=64)
    
    def __str__(self):
        return self.api_key
    

# Register user detail
class User(models.Model):
    username = models.CharField(max_length=32, primary_key=True)
    email = models.CharField(max_length=64)
    phone = models.CharField(max_length=12, null=True)
    registerd_api = models.OneToOneField(API, on_delete=models.CASCADE)
