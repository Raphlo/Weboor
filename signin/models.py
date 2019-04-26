from django.db import models

class NewUser(models.Model):
    username = models.CharField(min_length=6, max_length=30)
    password = models.CharField(min_length=8, max_length=30)
    email = models.EmailField(max_length=100, \
    message="Enter a valid Email address.")


class UserParameter(models.Model):
    name = models.CharField(max_length=42)
    age = models.IntegerField(max_length=3)
    sex = models.CharField(choices="male, female")
    birthdate = models.IntegerField(max_length=4)
