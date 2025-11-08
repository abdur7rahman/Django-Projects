from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=2000)
    content = RichTextField()
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Blog,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
