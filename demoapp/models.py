from django.db import models

# Create your models here.
class IrisData(models.Model):
  email = models.CharField(max_length=121)
  sepal_length = models.CharField(max_length=10)
  sepal_width = models.CharField(max_length=10)
  petal_length = models.CharField(max_length=10)
  petal_width = models.CharField(max_length=10)
  prediction_result = models.CharField(max_length=121)
  date = models.DateField()
  
  def __str__(self):
    return self.email
