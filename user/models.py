from django.contrib.auth.models import AbstractUser
from django.db import models
from base.model import BaseModel
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER = (
        ('M', 'male'),
        ('F', 'female'),
    )

    username = models.CharField(max_length=150, unique=True,
                                error_messages={
                                    'unique': _("A user with that phone already exists."),
                                },)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True)
    gender = models.CharField(choices=GENDER, max_length=10)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.get_username

    @property
    def get_full_name(self):
        return super().get_full_name()


class UserProfile(BaseModel):
    ADMIN = 1
    MODERATOR = 2
    NEWBIE = 3
    USER_ROLE = (
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (NEWBIE, 'Newbie'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=25)
    status = models.IntegerField(choices=USER_ROLE)

    def __str__(self):
        return f"Name: {self.user.username}" \
               f"Status: {self.status}"
