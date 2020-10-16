from django.shortcuts import render,redirect
from django.http import HttpResponse
from schoollist.models import teachers,students,grade
from django.contrib.admin.views.decorators import staff_member_required
from .forms import teacher_add_form, student_add_form, class_add_form, search_sort_form

# Create your views here.
@staff_member_required()
def index (request):
    teacher = teachers.objects.all()
    student = students.objects.all()
    classes = grade.objects.all()
    form = search_sort_form(request.POST or None)

    if form.is_valid():
        search_name = request.POST['search']
        sort_key = request.POST['sort']
        teacher = teachers.objects.filter(name__icontains= search_name).order_by(sort_key)
        context = {'teachers': teacher,
                   'students': student,
                   'classes': classes,
                   'form': form
                   }
        form = search_sort_form()
        return render(request, 'schoollist/home.html', context)

    context = {'teachers': teacher,
               'students': student,
               'classes': classes,
               'form': form
               }
    return render(request,'schoollist/home.html',context)

@staff_member_required
def teachers_add(request):
    teacher_form = teacher_add_form(request.POST or None, request.FILES or None)
    if teacher_form.is_valid():
        print(teacher_form.cleaned_data)
        try:
            obj = teachers.objects.create(**teacher_form.cleaned_data)
            teacher_form = teacher_add_form()
            obj.user = request.user
            return redirect("/")
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
        return redirect("/")

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
            return redirect("/")
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
    return redirect("/")

@staff_member_required
def student_delete(request, id):
    try:
        students.objects.get(pk = id).delete()
    except students.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/")

@staff_member_required
def class_delete(request, id):
    try:
        grade.objects.get(pk = id).delete()
    except grade.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/")

@staff_member_required
def teacher_deleteall (request):
    try:
        teachers.objects.all().delete()
    except teachers.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/")

@staff_member_required
def student_deleteall (request):
    try:
        students.objects.all().delete()
    except students.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/")

@staff_member_required
def class_deleteall (request):
    try:
        grade.objects.all().delete()
    except grade.DoesNotExist:
        return HttpResponse("It is already deleted, refresh the page")
    return redirect("/")

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
        return redirect("/")
    context = {"form": form,
               "class":obj
               }
    return render(request, 'schoollist/class_update_form.html', context)

def student_update(request, id):
    obj = students.objects.get(pk = id)
    form = student_add_form(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form": form,
               "student":obj
               }
    return render(request, 'schoollist/student_update_form.html', context)

def teacher_update(request, id):
    obj = teachers.objects.get(pk = id)
    form = teacher_add_form(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form": form,
               "teacher":obj
               }
    return render(request, 'schoollist/teacher_update_form.html', context)



