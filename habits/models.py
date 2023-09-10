#import self
from django.db import models
NULLABLE = {'blank': True, 'null': True}
# Create your models here.
class Habit(models.Model):
    name = models.CharField(max_length=150, verbose_name='название привычки',**NULLABLE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    place = models.CharField(max_length=150, verbose_name='место',**NULLABLE)
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='время',**NULLABLE)
    action = models.CharField(max_length=150, verbose_name='действие', **NULLABLE)
    lovely_habit_sign = models.BooleanField(default=True, **NULLABLE)
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE,verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(default=1, verbose_name='периодичность',**NULLABLE)
    award = models.CharField(max_length=150, verbose_name='вознаграждение',**NULLABLE)
    time_to_do = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='время на выполнение',**NULLABLE)
    publicity = models.BooleanField(default=True, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.user}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

# class Mailing(models.Model):
#     title = models.CharField(max_length=100, verbose_name="Тема письма", **NULLABLE)
#     content = models.TextField(verbose_name='Содержимое письма', **NULLABLE)
#
#
#     class Meta:
#         verbose_name = "Сообщение"
#         verbose_name_plural = "Сообщения"
#
#     def __str__(self):
#         return f"{self.title}"