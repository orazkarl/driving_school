from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from landing.models import School, Group, DrivingCategories, Lesson
from driving_school import settings


class User(AbstractUser):
    first_name = models.CharField('Имя', max_length=150, null=True, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, null=True, blank=True)
    id_passport = models.PositiveIntegerField('ИИН', validators=[MaxValueValidator(999999999999)], null=True,
                                              blank=True, default=None)
    number_passport = models.PositiveIntegerField('Номер пасспорта', validators=[MaxValueValidator(999999999)], null=True,
                                                  blank=True, default=None)
    dob = models.DateField('Дата рожения', null=True, blank=True)
    place_of_birth = models.CharField('Место рождения', max_length=150, null=True, blank=True)
    address = models.CharField('Адрес', max_length=150, null=True, blank=True)
    number_phone = models.PositiveIntegerField('Номер телефона', null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    USER_TYPE_CHOICES = (
        ('T', 'Учитель'),
        ('S', 'Ученик'),
    )

    # status = models.CharField('Статус', max_length=1, choices=USER_TYPE_CHOICES, default='S', blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)


class Teacher(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'


class Student(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(DrivingCategories, blank=True, null=True, on_delete=models.CASCADE,
                                  verbose_name='Категория', related_name='categoty')
    study_category = models.ForeignKey(DrivingCategories, blank=True, null=True, on_delete=models.CASCADE,
                                       verbose_name='Изучаемая категория', related_name='study_category')
    start_training = models.DateField('Начало обучение', null=True)
    graduation_training = models.DateField('Окончание обучение', null=True)

    class Meta:
        verbose_name = 'Учащиеся'
        verbose_name_plural = 'Учащиеся'

class Department_IA(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'ГАИ/УВД'
        verbose_name_plural = 'ГАИ/УВД'



class Grading(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    schools = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)
    lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.SET_NULL)
    date_of_grade = models.DateField('Дата', null=True, blank=True)
    grade = models.PositiveIntegerField('Оценка', null=True, blank=True)

    class Meta:
        verbose_name = 'Оценки'
        verbose_name_plural = 'Оценки'

