from django.db import models


# Create your models here.
class UserProfile(models.Model):
    end_year = models.DateField(null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=80, null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    insight = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=400, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.DateField(blank=True, null=True)
    impact = models.CharField(max_length=200, null=True, blank=True)
    added = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    likelihood = models.IntegerField(null=True, blank=True)
    objects = models.Model

    def __str__(self):
        return f"{self.topic}"
