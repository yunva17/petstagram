from django.db import models

# Create your models here.

class Board(models.Model):
    board_id = models.CharField(max_length=50, unique=True, null=True)
    content = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True)
