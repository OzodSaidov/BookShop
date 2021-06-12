from django.db import models
from django.contrib.auth.models import User
from base.model import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    publisher = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Title: {self.title}"


class Author(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Name: {self.name}"
