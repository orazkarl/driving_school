from django.contrib import admin
from django.forms import forms
from .models import School, Group, DrivingCategories, Lesson
from user_auth.models import Student, User, Teacher, Department_IA


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'is_active']

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Teacher.objects.filter(
                username=request.user.username) and not Department_IA.objects.filter(username=request.user.username):
            return True


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'schools', 'is_active']

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username):
            return True



@admin.register(DrivingCategories)
class DrivingCategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Teacher.objects.filter(
                username=request.user.username) and not Department_IA.objects.filter(username=request.user.username):
            return True

    def has_change_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True

    def has_add_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True

    def has_delete_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'schools', 'group', 'date_of_lesson', 'time_of_lesson']
    fieldsets = (
        (None, {'fields': ('name', 'group', 'date_of_lesson', 'time_of_lesson')}),
    )
    # def save_model(self, request, obj, form, change):
        # if not self.group.schools == self.schools:
        #     print(1)
        #     raise forms.ValidationError('Существует инстанс модели с некоторыми параметрами!')
        # super().save_model(request, obj, form, change)
    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         if not self.group.schools == self.schools:
    #             raise forms.ValidationError('Существует инстанс модели с некоторыми параметрами!')


    def get_queryset(self, request):
        query_set = Lesson.objects.all()
        if Student.objects.filter(username=request.user.username):
            if Student.objects.filter(group=request.user.student.group):
                query_set = Lesson.objects.filter(group=request.user.student.group)
                return query_set
        return query_set

    def has_module_permission(self, request, obj=None):
        if not Department_IA.objects.filter(username=request.user.username):
            return True

    def has_change_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True

    def has_add_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True

    def has_delete_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True
