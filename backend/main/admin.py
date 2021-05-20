from django.contrib import admin
from main import models

# Register your models here.
admin.site.register([models.Post,models.Likes,models.Comment,models.Friends])