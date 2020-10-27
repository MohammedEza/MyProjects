from django.db import models

from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class teachers (models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    age = models.IntegerField(blank=False, null=False)
    qualification = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField( max_length= 20, blank=False, unique=True, null= False)
    image = models.ImageField(upload_to='images/', null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)


class grade (models.Model):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


    sectionchoice = [
        (A, "A"),
        (B, "B"),
        (C, "C"),
        (D, "D"),
        (E, "E")

    ]

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    grade = models.IntegerField(blank=False, null=False)
    section = models.CharField(max_length=100, null=False, blank=False, choices=sectionchoice)
    teacher = models.OneToOneField(teachers, null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return (str(self.grade)+self.section)



    class Meta:
        ordering = ('id',)
        unique_together = ('grade', 'section',)

class students (models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=False, null=False)
    grade = models.ForeignKey(grade, null= True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=20, blank=False, unique=True, null=False)
    address = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
