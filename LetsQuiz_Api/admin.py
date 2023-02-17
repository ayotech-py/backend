from django.contrib import admin
from .models import Jwt, OrganizeQuiz

admin.site.register((Jwt, OrganizeQuiz))
