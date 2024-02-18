from django.contrib import admin
from .models import UserAccount, Activity

admin.site.register(Activity)
admin.site.register(UserAccount)
