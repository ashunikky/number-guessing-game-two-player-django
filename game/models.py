from django.db import models

# Create your models here.
class player(models.Model):
    
    firstname=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=200,null=True)
    guessed_number=models.IntegerField(null=True)
    attempts=models.IntegerField(null=True)
    

    def __str__(self):
        return str(self.id)

class gamemaster(models.Model):
    
    selected_number=models.IntegerField(null=True)
    player=models.OneToOneField(player,on_delete=models.CASCADE,null=True,related_name ='player')

    def __str__(self):
        return str(self.id) 
    