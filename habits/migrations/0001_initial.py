# Generated by Django 4.2.4 on 2023-09-04 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тема письма')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='название привычки')),
                ('place', models.CharField(blank=True, max_length=150, null=True, verbose_name='место')),
                ('time', models.CharField(blank=True, max_length=150, null=True, verbose_name='время')),
                ('action', models.CharField(blank=True, max_length=150, null=True, verbose_name='действие')),
                ('lovely_habit_sign', models.BooleanField(blank=True, default=True, null=True)),
                ('periodicity', models.CharField(blank=True, max_length=150, null=True, verbose_name='периодичность')),
                ('award', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('time_to_do', models.CharField(blank=True, max_length=150, null=True, verbose_name='время на выполнение')),
                ('publicity', models.BooleanField(blank=True, default=True, null=True)),
                ('associated_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
