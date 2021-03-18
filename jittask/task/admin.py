from django.contrib import admin
from .models import Profile, Unit, Client, Task

# Register your models here.
admin.site.register(Profile)
admin.site.register(Unit)
admin.site.register(Client)
admin.site.register(Task)