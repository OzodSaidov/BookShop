from django.contrib.auth.models import AbstractUser
from django.db import models
from base.model import BaseModel


class User(AbstractUser):
    GENDER = (
        ('M', 'male'),
        ('F', 'female'),
    )

    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(choices=GENDER, max_length=10)

    @property
    def get_full_name(self):
        return super(User, self).get_full_name()


class UserProfile(BaseModel):
    ADMIN = 1
    MODERATOR = 2
    NEWBIE = 3
    USER_ROLE = (
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (NEWBIE, 'Newbie'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    status = models.IntegerField(choices=USER_ROLE)

    def __str__(self):
        return f"Name: {self.user.username}" \
               f"Status: {self.status}"
