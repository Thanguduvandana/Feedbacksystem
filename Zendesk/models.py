from django.db import models
class ZendeskUser(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def _str_(self):
        return self.name

# Create your models here.
