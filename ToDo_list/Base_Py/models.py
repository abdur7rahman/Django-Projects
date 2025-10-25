from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    complete_status = models.BooleanField(default=False)
    Created_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete_status']
