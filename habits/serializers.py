from rest_framework import serializers
#from rest_framework.fields import SerializerMethodField
#from rest_framework.generics import get_object_or_404

from habits.models import Habit
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#from habits.tasks import about_subscription
from habits.validators import lovely_habit_sign1, lovely_habit_sign2, no_award, validator_prohibited_habit
#from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token


class HabitSerializer(serializers.ModelSerializer):
    lovely_habit_sign = serializers.CharField(validators=[lovely_habit_sign1, lovely_habit_sign2], read_only=True)
    associated_habit = serializers.CharField(validators=[no_award, validator_prohibited_habit], read_only=True)
    
    class Meta:
        model = Habit
        fields = '__all__'


# class CourseSerializer(serializers.ModelSerializer):
#
#     def subscription(self, validated_data, request):
#         user = get_object_or_404(User, pk=request.data.get('user'))
#         subscription = self.context['subscription']
#         validated_data['subscription'] = subscription
#         about_subscription.delay(user.username)
#         return subscription


