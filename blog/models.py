from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        txt = '{0}'
        return txt.format(self.title)
    
