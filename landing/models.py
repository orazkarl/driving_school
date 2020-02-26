from django.db import models
from django.core.validators import MaxValueValidator
# from .admin import Student
from driving_school import settings

# Create your models here.

class School(models.Model):
    name = models.CharField('Название', max_length=100, null=True, blank=True)
    address = models.CharField('Адрес', max_length=100, null=True, blank=True)
    is_active = models.BooleanField('Активность', default=False)

    def __str__(self):
        return 'Школа "{}"'.format(self.name)

    class Meta:
        verbose_name = 'Учебные заведения'
        verbose_name_plural = 'Учебные заведения'


class Group(models.Model):
    name = models.CharField('Название', max_length=100, null=True, blank=True)
    schools = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField('Активность', default=False)

    def __str__(self):
        return 'Группа "{}"'.format(self.name)


    class Meta:
        verbose_name = 'Учебные классы'
        verbose_name_plural = 'Учебные классы'

class DrivingCategories(models.Model):
    name = models.CharField('Название', max_length=100, null=True, blank=True)

    def __str__(self):
        return 'Категоия - "{}"'.format(self.name)

    class Meta:
        verbose_name = 'Водительские категории'
        verbose_name_plural = 'Водительские категории'

class Lesson(models.Model):
    name  = models.CharField('Тема занятия', max_length=100, null=True, blank=True)
    schools = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    group =  models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)
    date_of_lesson = models.DateField('Дата урока', null=True, blank=True)
    time_of_lesson = models.TimeField('Время', null=True, blank=True, default='09:00')

    def __str__(self):
        return 'Урок - "{}"'.format(self.name)

    class Meta:
        verbose_name = 'Занятия'
        verbose_name_plural = 'Занятия'
