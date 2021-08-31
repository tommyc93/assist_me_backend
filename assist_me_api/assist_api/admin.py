from django.contrib import admin

# Register your models here.
from .models import Budget
admin.site.register(Budget)

from .models import Task
admin.site.register(Task)

from .models import User
admin.site.register(User)
