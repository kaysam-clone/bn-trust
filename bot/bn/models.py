from django.db import models

# Create your models here.



class DonnaUsers(models.Model):
    username = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username


class MohammedUsers(models.Model):
    username = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username


class GuestUsers(models.Model):
    username = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username