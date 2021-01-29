# import the standard Django Model
# from built-in library
from django.db import models


class FlashcardsModel(models.Model):
    frontside = models.CharField(max_length=24)
    backside = models.CharField(max_length=24)
    answer = models.CharField(max_length=44)

    def __str__(self):
        return self.frontside


class Person(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)


# declare a new model with a name "GeeksModel"
# class GeeksModel(models.Model):

    # fields of the model
    # title = models.CharField(max_length=200)
    # description = models.TextField()

    # renames the instances of the model
    # with their title name
    # def __str__(self):
        # return self.title
