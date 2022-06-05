from django.db import models

# Create your models here.
class Hh_Request(models.Model):
    keywords = models.TextField(blank=False)

    def __str__(self):
        return self.keywords

class Hh_Response(models.Model):
    request = models.ForeignKey(Hh_Request, on_delete=models.CASCADE)
    skill_name = models.TextField(blank=False)
    skill_count = models.PositiveIntegerField (blank=False)
    skill_persent = models.PositiveIntegerField (blank=False)

    def __str__(self):
        return f'{self.request} {self.skill_name} {self.skill_count} {self.skill_persent}%'