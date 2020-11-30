from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Id = models.URLField(primary_key=True)
    age = models.UUIDField(max_length=3)

    def __str__(self):
        return self.first_name
    def __str__(self):
        return self.last_name


class Volunteer(Person):
        phone_number = models.UUIDField(max_length=10)

class Elderly(Person):
        phone_number = models.UUIDField(max_length=10)
        image = models.ImageField(null=True, blank=True, )

class Maneger(models.Model):

        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        mail_adress = models.CharField(max_length=150)

class Review(models.Model):
        rating = models.IntegerField()
        description = models.TextField()
        volunteer_id = models.UUIDField()


def __str__(self):
        return self.description