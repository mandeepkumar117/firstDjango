from django.urls import path
from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance_records/', views.attendance_records, name='attendance_records'),
]
