from django.urls import path
from rest_framework.routers import DefaultRouter
from habits.apps import HabitsConfig
from habits.views import HabitViewSet, HabitCreateAPIView, HabitListAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name
router = DefaultRouter()
router.register(r'habits',HabitViewSet, basename='habits')
urlpatterns = [
                path('habits/create', HabitCreateAPIView.as_view(), name='habit-create'),
                path('habit/list', HabitListAPIView.as_view(), name='habit-list'),
                path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
                path('habit/destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-destroy'),


]+router.urls