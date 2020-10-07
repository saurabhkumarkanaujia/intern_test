from django.db import models

class Job(models.Model):
    company_name=models.CharField(max_length=245)
    expiry_date_time=models.CharField(max_length=245)


# Create your models here.
