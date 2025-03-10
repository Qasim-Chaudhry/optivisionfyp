# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import random


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"

class ModelData(models.Model):
    model_uid = models.CharField(max_length=255, unique=True)
    name=models.CharField(max_length=255, default='default_name')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description=models.CharField(max_length=255, default='default_description')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id


class Rating(models.Model):
    frame = models.ForeignKey(ModelData, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Optional: associate with a user
    rating = models.IntegerField()  # Rating value (1 to 5)
    review_comment=models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating for {self.frame.name} by {self.user.username} - {self.rating}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate with the user
    frame = models.ForeignKey(ModelData, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username} - {self.frame.name}"

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp_code = str(random.randint(100000, 999999))
        self.save()

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title