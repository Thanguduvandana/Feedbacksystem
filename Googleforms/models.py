from django.db import models
class GoogleForm(models.Model):
    form_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.title
    from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
