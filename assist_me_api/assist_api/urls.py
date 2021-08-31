from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/budget', views.BudgetList.as_view(), name='budget_list'),
    path('api/budget/<int:pk>', views.BudgetDetail.as_view(), name='budget_detail'),
    path('api/task', views.TaskList.as_view(), name='Task_list'),
    path('api/task/<int:pk>', views.TaskDetail.as_view(), name='Task_detail'),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/users/login', csrf_exempt(views.check_login), name="check_login"),
]
