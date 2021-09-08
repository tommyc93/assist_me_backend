from rest_framework import generics

from .serializers import BudgetSerializer
from .models import Budget

from .serializers import ExpenseSerializer
from .models import Expense

from .serializers import TaskSerializer
from .models import Task

from .serializers import DailySerializer
from .models import Daily

from .serializers import UserSerializer
from .models import User

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
import json
# Create your views here.

class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all().order_by('id')
    serializer_class = BudgetSerializer

class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all().order_by('id')
    serializer_class = BudgetSerializer

class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all().order_by('id')
    serializer_class = ExpenseSerializer

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all().order_by('id')
    serializer_class = ExpenseSerializer

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

class DailyList(generics.ListCreateAPIView):
    queryset = Daily.objects.all().order_by('id')
    serializer_class = DailySerializer

class DailyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Daily.objects.all().order_by('id')
    serializer_class = DailySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

### User Auth
def check_login(request):

    if request.method=='GET':
        return JsonResponse({})

    if request.method=='PUT':

        jsonRequest = json.loads(request.body)
        username = jsonRequest['username']
        password = jsonRequest['password']
        if User.objects.get(username=username):
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return JsonResponse({'id': user.id, 'username': user.username, 'use': user.use})
            else:
                return JsonResponse({})
        else:
            return JsonResponse({})
