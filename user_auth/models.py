from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from landing.models import School, Group, DrivingCategories, Lesson
from driving_school import settings


class User(AbstractUser):
    name = models.CharField('ФИО', max_length=150, null=True, blank=True)
    # last_name = models.CharField('Фамилия', max_length=150, null=True, blank=True)
    id_passport = models.CharField('ИИН', max_length=12, null=True, blank=True, default=None)
    number_passport = models.PositiveIntegerField('Номер пасспорта', validators=[MaxValueValidator(999999999)],
                                                  null=True,
                                                  blank=True, default=None)
    dob = models.DateField('Дата рожения', null=True, blank=True)
    place_of_birth = models.CharField('Место рождения', max_length=150, null=True, blank=True)
    address = models.CharField('Адрес', max_length=150, null=True, blank=True)
    number_phone = models.CharField('Номер телефона', null=True, blank=True, max_length=50)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Школа')
    is_staff = models.BooleanField('Статус персонала', default=True,
                                   help_text='Отметьте, если пользователь может входить в административную часть сайта.')
    is_superuser = models.BooleanField('Статус суперпользователя', default=True,
                                       help_text='Указывает, что пользователь имеет все права без явного их назначения. ')
    USER_TYPE_CHOICES = (
        ('T', 'Учитель'),
        ('S', 'Ученик'),
    )

    # status = models.CharField('Статус', max_length=1, choices=USER_TYPE_CHOICES, default='S', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)


class Teacher(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,
                                verbose_name='Учитель')

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'


# class StudentFile(models.Model):
#     file = models.FileField('Файл', null=True, blank=True)
#     title_file = models.CharField('Названия документа', null=True, blank=True, max_length=150)
#
#     def __str__(self):
#         return '%s, %s' % (self.file, self.title_file)


class Student(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Учебный класс')
    category = models.ForeignKey(DrivingCategories, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Категория', related_name='category')
    study_category = models.ForeignKey(DrivingCategories, blank=True, null=True, on_delete=models.CASCADE,
                                       verbose_name='Изучаемая категория', related_name='study_category')
    start_training = models.DateField('Начало', null=True, blank=True)
    graduation_training = models.DateField('Окончание', null=True, blank=True)

    # file = models.ForeignKey(StudentFile, null=True,blank=True, on_delete=models.CASCADE)
    # file = models.FileField('Документ',null=True, blank=True, default='default_post_image.jpg', upload_to='media/', )
    # title_file = models.CharField('Названия документа', null=True, blank=True, max_length=150)

    def save(self, *args, **kwargs):
        if self.group:
            self.school = self.group.schools
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Учащиеся'
        verbose_name_plural = 'Учащиеся'


class StudentFile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Ученик')
    title_file = models.CharField('Названия документа', null=True, blank=True, max_length=150)
    file = models.FileField('Файл', null=True, blank=True, default='default_post_image.jpg', upload_to='media/')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документ'

    def __str__(self):
        return self.title_file


class Department_IA(User):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'Адм. Пол. - Спец. Цон.'
        verbose_name_plural = 'Адм. Пол. Спец. Цон.'


class Grading(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Ученик')
    # schools = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    # group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL)
    # lesson = models.ForeignKey(Lesson, null=True, blank=True, on_delete=models.SET_NULL)
    lesson_name = models.CharField('Дисциплина', blank=True, null=True, max_length=150)
    date_of_grade = models.DateField('Дата', null=True, blank=True)
    grade = models.PositiveIntegerField('Оценка', null=True, blank=True)

    class Meta:
        verbose_name = 'Оценки'
        verbose_name_plural = 'Оценки'
