from django.db import models
class Feedback(models.Model):
    name = models.CharField(max_length=255)
    feedback = models.CharField(max_length=255)
    
    def _str_(self):
        return self.title

# Create your models here.
