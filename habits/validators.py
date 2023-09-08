from rest_framework import serializers

from habits.models import Habit


#Исключить одновременный выбор связанной привычки и указания вознаграждения
def validator_prohibited_habit(value1):
    if value1 == True and Habit.lovely_habit_sign != True:
        raise serializers.ValidationError('У связанной привычки необходимо наличие признака приятной привычки')

def no_award(value1):
    if value1== True and Habit.award != None:
        raise serializers.ValidationError('У связанной привычки не может быть вознаграждения')

def lovely_habit_sign1(value1):
    if value1 == True and Habit.award != None:
        raise serializers.ValidationError('У приятной привычки не может быть вознаграждения')

def lovely_habit_sign2(value1):
    if value1 == True and Habit.associated_habit != None:
        raise serializers.ValidationError('У приятной привычки не может быть связанной привычки')
