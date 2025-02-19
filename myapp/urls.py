from django.urls import path
from .import views
 
urlpatterns = [
    path('contact/',views.contact,name="contact"),
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('courses/',views.courses,name="courses"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"), 
    path('course-details/<int:parent_id>/<int:id>/',views.course_details,name='detailx'),
    path('send-otp/',views.send_otp,name="send-otp"),
    path('otp-verify/',views.otp_verify,name="otp-verify"),
    path('password/',views.password,name="password")   
   
    ]

 