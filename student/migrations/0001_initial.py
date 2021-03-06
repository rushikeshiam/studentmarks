# Generated by Django 3.2.3 on 2021-08-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('RollNo', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=40)),
                ('Class', models.CharField(max_length=40)),
                ('School', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField()),
                ('Address', models.CharField(max_length=240)),
            ],
            options={
                'db_table': 'StudentInfo',
            },
        ),
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maths', models.IntegerField()),
                ('Physics', models.IntegerField()),
                ('Chemistry', models.IntegerField()),
                ('Biology', models.IntegerField()),
                ('English', models.IntegerField()),
                ('RollNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentinfo')),
            ],
            options={
                'db_table': 'StudentAcademics',
            },
        ),
    ]
