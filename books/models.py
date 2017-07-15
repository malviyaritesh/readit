from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=150)
  author = models.CharField(max_length=70)
  review = models.TextField(blank=True, null=True)
  data_reviewed = models.DateTimeField()
  is_favourite = models.BooleanField(default=False)
