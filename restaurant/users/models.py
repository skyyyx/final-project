from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class Recommend(models.Model):
    ROLE = {
        "Admin": "admin",
        "Customer": "users",
        "ShopOwner": "shop"
    }

    DISTANCE = {
        "S": "1 km",
        "M": "5 km",
        "L": "unlimited"
    }

    FOOD = {
        "N": "north",
        "E": "northeast",
        "S": "south",
        "C": "central"
    }

    MOOD = {
        "N": "nature",
        "A": "air conditioner",
        "S": "street Food"
    }

    distance = models.CharField(max_length=1, choices=DISTANCE, blank=True)
    food = models.CharField(max_length=1, choices=FOOD, blank=True)
    mood = models.CharField(max_length=1, choices=MOOD, blank=True)
    updateDate = models.DateField()
    image = models.ImageField(upload_to="recommends")
    isSelected = models.BooleanField(blank=True)
    recommendUser = models.CharField(max_length=100)

    def __str__(self):
        return self.distance,self.food,self.mood

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    ROLE = {
        "Admin": "admin",
        "Customer": "users",
        "ShopOwner": "shopOwner"
    }

    firstName = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=10, choices=ROLE)

    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName','role']

    def __str__(self):
        return self.email

