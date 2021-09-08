from django.contrib import admin

# Register your models here.
from .models import Budget
admin.site.register(Budget)

from .models import Expense
admin.site.register(Expense)

from .models import Task
admin.site.register(Task)

from .models import Daily
admin.site.register(Daily)

from .models import User
admin.site.register(User)
