from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

# class Account(AbstractUser):
#     score = models.IntegerField(default=0)

# email_verified = models.BooleanField(default=False)
# email_token = models.CharField(max_length=100, null=True, default=0)

# def verify_email(self):
#     self.email_verified = True
#     self.save()

# def retract_email_verification(self):
#     self.email_verified = False
#     self.save()

# def generate_email_token(self):
#     letters = string.ascii_lowercase
#     token = ''.join(random.choice(letters) for i in range(10))
#     first_letter = self.username[0]
#     last_letter = self.username[-1]
#     middle_letters = self.username[1:-1]
#     final_token = first_letter + token[0:5] + middle_letters + token[5:-1] + last_letter
#     self.email_token = final_token
#     self.save()
#     return final_token
