# Generated by Django 3.1.2 on 2020-10-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoollist', '0002_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('section', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
