# Generated by Django 4.1.4 on 2023-01-24 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.book')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='Stud_Password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='Stud_Semester',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Issue_Book',
        ),
        migrations.AddField(
            model_name='issuebook',
            name='Student_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Libraryapp.student'),
        ),
    ]
