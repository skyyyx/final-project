from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class Activity(models.Model):
    ROLE = {
        "Admin": "admin",
        "Personnel": "users",
        "Officer": "officer"
    }

    DISTANCE = {
        "S": "1 km",
        "M": "5 km",
        "L": "unlimited"
    }

    FOOD = {
        "O": "north",
        "E": "northeast",
        "T": "south",
        "L": "central"
    }

    MOOD = {
        "U": "nature",
        "A": "air conditioner",
        "F": "street Food"
    }
    distance = models.CharField(max_length=1, choices=DISTANCE, blank=True, null=True)
    mood = models.CharField(max_length=1, choices=MOOD, blank=True, null=True)
    food = models.CharField(max_length=1, choices=FOOD, blank=True, null=True)
    updateDate = models.DateTimeField()
    isSelected = models.BooleanField(blank=True)
    activityUser = models.CharField(max_length=100)

    def __str__(self):
        if self.distance == "S":
            return "< 1 กิโลเมตร" + " User id : " + self.activityUser + " Status : " + self.status
        if self.distance == "M":
            return "< 5 กิโลเมตร" + " User id : " + self.activityUser + " Status : " + self.status
        if self.distance == "L":
            return "ไม่จำกัด" + " User id : " + self.activityUser + " Status : " + self.status
        if self.food == "O":
            return "เหนือ" + " User id : " + self.activityUser + " Status : " + self.status
        if self.food == "E":
            return "อีสาน" + " User id : " + self.activityUser + " Status : " + self.status
        if self.food == "T":
            return "ใต้" + " User id : " + self.activityUser + " Status : " + self.status
        if self.food == "L":
            return "กลาง" + " User id : " + self.activityUser + " Status : " + self.status
        if self.mood == "U":
            return "ธรรมชาติ" + " User id : " + self.activityUser + " Status : " + self.status
        if self.mood == "A":
            return "แอร์" + " User id : " + self.activityUser + " Status : " + self.status
        if self.mood == "F":
            return "สตรีทฟู้ด" + " User id : " + self.activityUser + " Status : " + self.status
       

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
        "Personnel": "users",
        "Officer": "officer"
    }

    firstName = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=10, choices=ROLE, blank=True)

    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName','role']

    def __str__(self):
        return self.email

class Shop(AbstractBaseUser, PermissionsMixin):
    ROLE = {
        "Admin": "admin",
        "Personnel": "users",
        "Officer": "officer"
    }

    firstName = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=10, choices=ROLE, blank=True)

    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName','role', ]

    def __str__(self):
        return self.email