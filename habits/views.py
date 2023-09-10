from datetime import datetime

from django.shortcuts import render
from tasks import habits_notification
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions.permissions import IsOwner, IsModerator
from users.serializers import  MyTokenObtainPairSerializer
from habits.serializers import HabitSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model

@login_required(login_url='/users/login')
def secure(request):
    user = request.user
    return render(request, 'secure.html', {'email': user.email})


# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated)


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]
    def new_notification(self, serializer):
        Habit.time.day = serializer.save()
        current_dateTime = datetime.now()
        if int(current_dateTime.day) - int(Habit.time.day)>= 7:
            habits_notification.delay(Habit.user)

class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = HabitPaginator

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]

class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = (IsAuthenticated)