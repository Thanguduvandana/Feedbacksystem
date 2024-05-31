from django.db import models
class SurveyMonkeySurvey(models.Model):
    survey_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.title

# Create your models here.
