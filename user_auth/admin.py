from django.contrib import admin
from .models import User, Student, Teacher, Department_IA, Grading, StudentFile
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'ALDIYAR-AVTO'


# @admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (('Personal info'), {'fields': (
            'first_name', 'last_name', 'id_passport', 'number_passport', 'dob', 'place_of_birth', 'address',
            'number_phone',
            'school')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      )}),

    )

    list_display = (
        'username', 'email', 'first_name', 'last_name', 'id_passport', 'number_passport', 'dob',
        'place_of_birth', 'address',
        'number_phone',
        'school')

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Teacher.objects.filter(
                username=request.user.username) and not Department_IA.objects.filter(username=request.user.username):
            return True


@admin.register(Student)
class StudentAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'dob', 'category', 'study_category', 'start_training',
        'graduation_training',
        'address',
        'number_phone',
        'school',
        'group',
        'file',
        'title_file',

    )
    list_filter = ['study_category', 'category']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': (
            'username', 'first_name', 'last_name', 'id_passport', 'address', 'number_phone', 'group',
            'category',
            'study_category', 'start_training',
            'graduation_training', 'file',
            'title_file')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )




    def get_queryset(self, request):
        query_set = Student.objects.all()
        if Student.objects.filter(username=request.user.username):
            query_set = Student.objects.filter(username=request.user.username)
            return query_set
        return query_set

    def has_module_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username):
            return True

    def has_add_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username):
            return True

    def has_delete_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username):
            return True


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'id_passport', 'number_passport', 'dob',
        'place_of_birth', 'address',
        'number_phone',
        'school')

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username):
            return True

    def get_queryset(self, request):
        query_set = Teacher.objects.all()
        if Teacher.objects.filter(username=request.user.username):
            query_set = Teacher.objects.filter(username=request.user.username)
            return query_set
        return query_set

    def has_add_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username) and not Teacher.objects.filter(username=request.user.username):
            return True

    def has_delete_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username) and not Teacher.objects.filter(username=request.user.username):
            return True

    def has_change_permission(self, request, obj=None):
        if not Department_IA.objects.filter(username=request.user.username):
            return True


@admin.register(Department_IA)
class DepartmentAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'address', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': (
            'username', 'first_name', 'address',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )

    def has_module_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Teacher.objects.filter(
                username=request.user.username):
            return True

    def get_queryset(self, request):
        query_set = Department_IA.objects.all()
        if Department_IA.objects.filter(username=request.user.username):
            query_set = Department_IA.objects.filter(username=request.user.username)
            return query_set
        return query_set

    def has_add_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username) and not Teacher.objects.filter(username=request.user.username):
            return True

    def has_delete_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Department_IA.objects.filter(
                username=request.user.username) and not Teacher.objects.filter(username=request.user.username):
            return True

    def has_change_permission(self, request, obj=None):
        if not Student.objects.filter(username=request.user.username) and not Teacher.objects.filter(
                username=request.user.username):
            return True


@admin.register(Grading)
class GradingAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson_name', 'grade', 'date_of_grade')

    def get_queryset(self, request):
        query_set = Grading.objects.all()
        if Student.objects.filter(username=request.user.username):
            query_set = Grading.objects.filter(student=request.user)
            return query_set
        return query_set

    def has_module_permission(self, request):
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


# @admin.register(StudentFile)
# class StudentFileAdmin(admin.ModelAdmin):
#     list_display = ['file', 'title_file']


from django.contrib.auth.models import Group

admin.site.unregister(Group)
# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()
