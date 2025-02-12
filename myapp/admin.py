
from django.contrib import admin
from .models import Courses,Registration
# # # Register your models here.
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display=('id','courses_name','parent_id','details_name','duration','content')
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
   list_display=('full_name','dob','gender','qualification','course','mobile','email','guardian_mobile','mode','location','guardian_name','guardian_occupation','preferred_timings','address','country','state','city','pin')
    
