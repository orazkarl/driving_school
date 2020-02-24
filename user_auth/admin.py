from django.contrib import admin
from .models import User, Student, Teacher, Department_IA
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'ALDIYAR-AVTO'


@admin.register(User)
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

    # def has_module_permission(self, request, obj=None):
    #     if not Student.objects.filter(username=request.user.username):
    #         return True


@admin.register(Student)
class StudentAdmin(UserAdmin):

    list_display = (
        'username', 'email', 'first_name', 'last_name', 'dob', 'category', 'study_category', 'start_training',
        'graduation_training',
        'address',
        'number_phone',
        'school')
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (('Personal info'), {'fields': (
    #         'username', 'first_name', 'last_name', 'id_passport', 'address', 'number_phone', 'school', 'category',
    #         'study_category', 'start_training',
    #         'graduation_training',)}),
    #     (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    #
    # )

    # def has_module_permission(self, request, obj=None):
    #     return True

    def has_view_permission(self, request, obj=None):
        return True
    #

    def has_change_permission(self, request, obj=None):
        # if not Student.objects.filter(username=request.user.username):
        #     return True
        return False
    #
    # def has_add_permission(self, request, obj=None):
    #     if Student.objects.filter(username=request.user.username):
    #         return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     if Student.objects.filter(username=request.user.username):
    #         return False




@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'id_passport', 'number_passport', 'dob',
        'place_of_birth', 'address',
        'number_phone',
        'school')




@admin.register(Department_IA)
class DepartmentAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'address', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': (
            'username', 'first_name', 'address',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )

