from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('teacher-add',views.teachers_add, name = 'teacher_form'),
    path('student-add',views.students_add, name = 'student_form'),
    path('class-add',views.class_add, name = 'class_form'),
    path('teacher-delete/<int:id>',views.teacher_delete, name= 'teacher_delete'),
    path('student-delete/<int:id>',views.student_delete, name= 'student_delete'),
    path('class-delete/<int:id>',views.class_delete, name= 'class_delete'),
    path('teacher-delete-all',views.teacher_deleteall, name= 'teacher_deleteall'),
    path('student-delete-all',views.student_deleteall, name= 'student_deleteall'),
    path('class-delete-all',views.class_deleteall, name= 'class_deleteall'),
    path('teacher-image/<int:id>',views.view_image, name= 'image'),
    path('teacher-detail/<int:id>',views.teacher_detail, name= 'teacher_detail'),
    path('class-detail/<int:id>',views.class_detail, name= 'class_detail'),
    path('student-detail/<int:id>',views.student_detail, name= 'student_detail'),
    path('class-update/<int:id>',views.class_update, name= 'class_update'),
    path('teacher-update/<int:id>',views.teacher_update, name= 'teacher_update'),
    path('student-update/<int:id>',views.student_update, name= 'student_update')
]