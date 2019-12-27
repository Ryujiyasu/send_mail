from django.db import models

# Create your models here.


class Gmail(models.Model):
    gmail=models.EmailField("GMAILアドレス")
    password=models.CharField("password",max_length=15)

