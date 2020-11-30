from django.db import models


class Volunteer(models.Model):
    #objects = None
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    image = models.ImageField(null=True, blank=True, )

    def __str__(self):
        return self.first_name
    def __str__(self):
        return self.last_name


class Elderly(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.UUIDField(primary_key=True)
    phone_Number = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    image = models.ImageField(null=True, blank=True, )


class Maneger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Review(models.Model):
    rating = models.IntegerField()
    description = models.TextField()
    volunteer_id = models.UUIDField()

    def __str__(self):
        return self.description