from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     phone = models.CharField(null=False)
#     data_rojdeniya = models.DateField(null=False)
#     email = models.EmailField(unique=True)
#     data_dobavleniya = models.DateTimeField(auto_now_add=True)
    
    
#     def __str__(self):
#         return self.username



class Message(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.username}: {self.text[:20]}"

    
    

