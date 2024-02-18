from django.contrib import admin
from .models import UserAccount, Recommend

admin.site.register(Recommend)
admin.site.register(UserAccount)
