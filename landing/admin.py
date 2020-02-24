from django.contrib import admin
from .models import School, Group, DrivingCategories, Lesson, Grading
from user_auth.models import Student, User, Teacher, Department_IA


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'is_active']

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'schools', 'is_active']

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True

@admin.register(DrivingCategories)
class DrivingCategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'schools', 'group', 'date_of_lesson', 'time_of_lesson']

@admin.register(Grading)
class GradingAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'grade', 'date_of_grade']

