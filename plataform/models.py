from django.db import models
from accounts.models import User  # import User model made by Nelzio


# member model
class Member(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=255, blank=True, null=True)
