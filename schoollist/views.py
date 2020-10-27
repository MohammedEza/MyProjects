from django.shortcuts import render,redirect
from django.http import HttpResponse
from schoollist.models import teachers,students,grade
from django.contrib.admin.views.decorators import staff_member_required
from .forms import teacher_add_form, student_add_form, class_add_form, search_sort_form
from django.contrib.auth import logout
from django.core.paginator import Paginator
# Create your views here.
@staff_member_required()
def index (request):

    form = search_sort_form(request.POST or None)
    if form.is_valid():
        search_name = request.POST['search']
        sort_key = request.POST['sort']
        teacher = teachers.objects.filter(name__icontains= search_name).order_by(sort_key)
        context = {


                   'form': form
                   }
        form = search_sort_form()
        return render(request, 'schoollist/home.html', context)

    context = {


               'form': form
               }
    return render(request,'schoollist/home.html',context)


@staff_member_required()
def teacher_table(request):
    sort_key = request.GET.get('sort') or 'id'
    teacher = teachers.objects.all().order_by(sort_key)
    teacher_paginator = Paginator(teacher,5)
    page_num = request.GET.get('page') or 1
    teacher_page = teacher_paginator.get_page(page_num)
    form = search_sort_form(request.POST)
    context = {
        'teachers':teacher_page,
        'form': form,
    }
    if form.is_valid():
        search_name= request.GET.get('search') or ""
        #print(search_name)
        teacher = teachers.objects.filter(name__icontains=search_name).order_by(sort_key)
        form = search_sort_form()
        context ={
            'teachers': teacher,
            'form': form,
            'sort_key':sort_key,
            'search': search_name

        }
        return render(request,'schoollist/teachertable.html', context)
    return render(request,'schoollist/teachertable.html', context)


@staff_member_required()
def student_table(request):
    student = students.objects.all()
    form = search_sort_form(request.POST or None)
    student_paginator = Paginator(student,5)
    page_num = request.GET.get('page') or 1
    student_page = student_paginator.get_page(page_num)

    context = {
        'students': student_page,
        'form': form
    }
    if form.is_valid():
        search_name = request.POST['search']
        student = students.objects.filter(name__icontains=search_name)
        context = {
            'students': student,
            'form': form
        }
        return render(request, 'schoollist/studenttable.html', context)
    return render(request, 'schoollist/studenttable.html', context)

@staff_member_required()
def class_table(request):
    grades = grade.objects.all()
    grades_paginator = Paginator(grades,5)
    page_num = request.GET.get('page') or 1
    grades_page = grades_paginator.get_page(page_num)


    context = {
        'classes': grades_page
    }
    return render (request, 'schoollist/classtable.html', context)



@staff_member_required
def teachers_add(request):
    teacher_form = teacher_add_form(request.POST or None, request.FILES or None)
    if teacher_form.is_valid():
        print(teacher_form.cleaned_data)
        try:
            obj = teachers.objects.create(**teacher_form.cleaned_data)
            teacher_form = teacher_add_form()
            obj.user = request.user
            return redirect("/teacher-table")
        except :
            teacher_form = teacher_add_form()
            return HttpResponse("Cannot add the data, the conditions are violated")
    context = {"form":teacher_form}
    return render(request, 'schoollist/teacher_form.html',context)


@staff_member_required
def students_add(request):
    form = student_add_form(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = students.objects.create(**form.cleaned_data)
        form = student_add_form()
        obj.user = request.user
        return redirect("/student-table")

    context = {"form":form}
    return render(request, 'schoollist/student_form.html',context)

@staff_member_required
def class_add(request):
    form = class_add_form(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        try:
            obj = grade.objects.create(**form.cleaned_data)
            form =class_add_form()
            obj.user = request.user
            return redirect("/class-table")
        except :
            form = class_add_form()
            return HttpResponse("Cannot add the data, the conditions are violated")
    context = {"form":form}
    return render(request, 'schoollist/class_form.html',context)

@staff_member_required
def teacher_delete(request, id):
    try:
        teachers.objects.get(pk = id).delete()
    except teachers.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/teacher-table")

@staff_member_required
def student_delete(request, id):
    try:
        students.objects.get(pk = id).delete()
    except students.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/student-table")

@staff_member_required
def class_delete(request, id):
    try:
        grade.objects.get(pk = id).delete()
    except grade.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/class-table")

@staff_member_required
def teacher_deleteall (request):
    try:
        teachers.objects.all().delete()
    except teachers.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/teacher-table")

@staff_member_required
def student_deleteall (request):
    try:
        students.objects.all().delete()
    except students.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/student-table")

@staff_member_required
def class_deleteall (request):
    try:
        grade.objects.all().delete()
    except grade.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/class-table")

@staff_member_required
def view_image(request, id):
    teacher = teachers.objects.get(pk = id)
    context = {'teacher' : teacher}
    return render (request, 'schoollist/view_image.html', context)

@staff_member_required
def teacher_detail(request, id):
    teacher = teachers.objects.get(pk = id)
    context = { 'teacher' : teacher }
    return render (request, 'schoollist/teacher_detail.html', context)

def class_detail(request, id):
    classes = grade.objects.get(pk = id)
    context = { 'class' : classes }
    return render (request, 'schoollist/class_detail.html', context)


def student_detail(request, id):
    student = students.objects.get(pk = id)
    context = { 'student' : student }
    return render (request, 'schoollist/student_detail.html', context)

def class_update(request, id):
    obj = grade.objects.get(pk = id)
    form = class_add_form(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/class-table")
    context = {"form": form,
               "class":obj
               }
    return render(request, 'schoollist/class_update_form.html', context)

def student_update(request, id):
    obj = students.objects.get(pk = id)
    form = student_add_form(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/student-table")
    context = {"form": form,
               "student":obj
               }
    return render(request, 'schoollist/student_update_form.html', context)

def teacher_update(request, id):
    obj = teachers.objects.get(pk = id)
    form = teacher_add_form(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/teacher-table")
    context = {"form": form,
               "teacher":obj
               }
    return render(request, 'schoollist/teacher_update_form.html', context)

def userlogout(request):
    logout(request)
    return redirect("/")



