from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

User = get_user_model

class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "Username",
        max_length = 150,
        unique = True,
        
       validators = [username_validator],
       error_messages = {
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(max_length=254, blank=False, unique = True)
    first_name = models.CharField(max_length = 30, blank = False)
    last_name = models.CharField(max_length = 50, blank = False)
