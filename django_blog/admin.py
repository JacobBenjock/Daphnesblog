from django.contrib import admin
from .models import Post, models
from django.utils import timezone
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Post)


