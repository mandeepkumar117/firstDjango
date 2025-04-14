from django.shortcuts import render,redirect
from .models import Student, Attendance
from datetime import date

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        student_class = request.POST.get('student_class')
        email = request.POST.get('email')

        Student.objects.create(name=name, roll_no=roll_no, student_class=student_class, email=email)
        
        return redirect('attendance_records')  # Yeh naye page par le jayega

    return render(request, 'add_students.html')

def mark_attendance(request):
    students = Student.objects.all()

    if request.method == "POST":
        student_id = request.POST.get('student')
        status = request.POST.get('status')

        if student_id and status:
            student = Student.objects.get(id=student_id)
            Attendance.objects.create(student=student, status=status, date=date.today())

    return render(request, 'mark_attendance.html', {'students': students})

def attendance_records(request):
    students = Student.objects.all()
    attendance = Attendance.objects.all()
    print(attendance)

    # Filter Logic
    student_id = request.GET.get('student')
    date = request.GET.get('date')

    if student_id:
        attendance = attendance.filter(student_id=student_id)
    if date:
        attendance = attendance.filter(date=date)

    return render(request, 'attendance_records.html', {'students': students, 'attendance': attendance})