from django.db import models

class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)