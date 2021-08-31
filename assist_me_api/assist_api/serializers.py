from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Budget
from .models import Task
from .models import User

class BudgetSerializer(serializers.ModelSerializers):
    class Meta:
        model = Budget
        fields = ('id', 'income', 'name', 'cost', 'note',)

class TaskSerializer(serializers.ModelSerializers):
    class Meta:
        model = Task
        fields = ('id', 'name', 'time', 'note', 'due',)

class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

    def create(self, validated_data):
        user = User.objects.create(
        username = validated_data['username'],
        use = validated_data['use'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    def update(self,instance,validated_data):
        user = User.objects.get(username=validated_data['username'])
        user.password = make_password(validated_data['password'])
        user.save()
        return user
        fields = ('id', 'username', 'password',)
