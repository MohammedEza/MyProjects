from django import forms

from .models import teachers, grade, students

"""sectionChoices = [
    ("A","A"),
    ("B","B"),
    ("C","C"),
    ("D","D"),
    ("E","E")


]"""

"""sectionChoices=[
    (grade.A , "A"),
    (grade.B , "B"),
    (grade.C , "C"),
    (grade.D , "D"),
    (grade.E , "E"),
]"""

SortChoices = [
    ("id","Date Added (oldest to latest)"),
    ("-id","Date Added (latest to oldest)"),
    ("age","Age (Ascending)"),
    ("-age","Age (Descending)"),
    ("name","Name (A to Z)"),
    ("-name","Name (Z to A)")
]
class teacher_add_form (forms.ModelForm):
    class Meta:
        model = teachers
        fields = ['name','age', 'qualification' , 'phone', 'image']


"""class teacher_add_form (forms.Form):

    name = forms.CharField()
    age = forms.IntegerField()
    qualification = forms.CharField()
    phone = forms.CharField()
    image = forms.ImageField()"""


class student_add_form (forms.ModelForm):
    class Meta:
        model = students
        fields = ['name','age', 'grade' , 'phone', 'address']

"""class student_add_form (forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    grade = forms.ModelChoiceField(queryset= grade.objects.all())
    phone = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)"""

"""class class_add_form (forms.Form):
    grade = forms.IntegerField()
    section = forms.CharField(widget= forms.Select(choices=sectionChoices))
    teacher = forms.ModelChoiceField(queryset= teachers.objects.all())"""

class class_add_form (forms.ModelForm):
    class Meta:
        model = grade
        fields= ['grade','section','teacher']


class search_sort_form (forms.Form):
    search = forms.CharField( label="", widget=forms.TextInput(attrs={'placeholder': 'Search Name'}), required= False)
    #sort = forms.CharField(widget=forms.Select(choices=SortChoices))