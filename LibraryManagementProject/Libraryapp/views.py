from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from Libraryapp.models import Student, Course, Book, IssueBook


# Create your views here.
def log_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    user_name = request.POST["txtusername"]
    user_pswd = request.POST["txtPswd"]

    user1=authenticate(username=user_name,password=user_pswd)


    if user1 is not None:
        if user1.is_superuser:
            return redirect('ahome')

    elif Student.objects.filter(Q(Stud_Name=user_name)& Q(Stud_Password=user_pswd)).exists():
        request.session['name']=user_name
        return render(request,'student_home.html')
    else:
        return render(request,'login.html',{'data':'Enter proper username and password'})


def admin_reg_fun(request):
    return render(request,'admin_register.html', {'data': ''})


def student_reg_fun(request):
    c1=Course.objects.all()
    return render(request,'student_register.html', {'course': c1})


def admin_regdata_fun(request):
    user_name = request.POST["txtUserName"]
    user_email = request.POST["txtemail"]
    user_pswd = request.POST["txtPswd"]

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request,'admin_register.html', {'data': 'Username,email,password already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_pswd)
        u1.save()
        return redirect('log')

def student_regdata_fun(request):
    s1=Student()
    s1.Stud_Name = request.POST["txtname"]
    s1.Stud_Phno = request.POST["txtPhno"]
    s1.Stud_Password = request.POST["txtpswd"]
    s1.Stud_Semester=request.POST["txtsemester"]
    s1.Stud_Course=Course.objects.get(Course_Name=request.POST["ddlcourse"])
    s1.save()
    return redirect('log')



def admin_home_fun(request):
    return render(request,'admin_home.html')


def student_home_fun(request):
    return render(request,'student_home.html')


def home_fun(request):
    return redirect('admin_home')


def addbook_fun(request):
    c1 = Course.objects.all()
    return render(request,'add_book.html',{'course': c1})


def displaybook_fun(request):
    b1 = Book.objects.all()
    return render(request,'display_book.html',{'course': b1})


def assign_fun(request):
    c1=Course.objects.all()
    return render(request,'assign_book.html',{'course':c1})



def readassigndata_fun(request):
    c1 = Course.objects.all()
    if request.method == 'POST':
        c2=Course.objects.get(Course_Name=request.POST['ddlcourse'])
        c=c2.id
        s1=Student.objects.filter(Q(Stud_Semester=request.POST['txtsem']) & Q(Stud_Course=c))
        b1=Book.objects.filter(Course_Id=c)

        return render(request,'assign_book.html',{'data':s1,'book':b1,'course':c1})
    return render(request,'assign_book.html',{'course':c1})


def assignbookdata_fun(request):
    i1 = IssueBook()
    i1.Student_Name=Student.objects.get(Stud_Name=request.POST['ddlsname'])
    i1.Book_name=Book.objects.get(Book_Name=request.POST['ddlbname'])
    i1.Start_Date=request.POST['tbsdate']
    i1.End_Date=request.POST['tbedate']
    i1.save()

    return redirect('assign')




def issuebook_fun(request):
    i1=IssueBook.objects.all()
    return render(request,'issuebook.html',{'data': i1})


def readbookdata_fun(request):
    b1=Book()
    b1.Book_Name=request.POST["txtBookName"]
    b1.Author_Name=request.POST["txtAuthorName"]
    b1.Course_Id=Course.objects.get(Course_Name=request.POST["ddlcourse"])
    b1.save()
    return redirect('ahome')


def update_fun(request,id):
    b1 = Book.objects.get(id=id)
    course=Course.objects.all()
    if request.method == 'POST':
        b1.Book_Name = request.POST["txtBookName"]
        b1.Author_Name = request.POST["txtName"]
        b1.Course_Id = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        b1.save()
        return redirect('display')

    return render(request, 'update.html', {'course': b1,'course_name':course})



def delete_fun(request,id):
    b1 = Book.objects.get(id=id)
    b1.delete()

    return redirect('display')

def log_out_fun(request):
    return redirect('log')


def update2_fun(request,id):
    i1=IssueBook.objects.get(id=id)
    b1=Book.objects.all()
    if request.method =='POST':
        i1.Student_Name = Student.objects.get(Stud_Name=request.POST['tbsname'])
        i1.Book_name = Book.objects.get(Book_Name=request.POST['ddlbname'])
        i1.Start_Date = request.POST['tbsdate']
        i1.End_Date = request.POST['tbedate']
        i1.save()
        return redirect('issue')

    return render(request,'updateissuebk.html',{'data':i1,'book':b1})


def delete2_fun(request,id):
    i1=IssueBook.objects.get(id=id)
    i1.delete()
    return redirect('issue')

def profile_fun(request):
    s1=Student.objects.get(Stud_Name=request.session['name'])
    return render(request, 'profile.html',{'data':s1})

def updatepro_fun(request,id):
    s1 = Student.objects.get(id=id)
    if request.method == 'POST':
        s1.Stud_Name = request.POST["tbsname"]
        s1.Stud_Phno = request.POST["tbsphno"]
        s1.Stud_sem = request.POST["tbssem"]
        s1.Stud_pass = request.POST["tbspswd"]
        s1.save()
        return redirect('profile')
    return render(request,'update_pro.html',{'data':s1})




def issuebkdet_fun(request):
    b1=IssueBook.objects.filter(Student_Name=Student.objects.get(Stud_Name=request.session['name']))

    return render(request,'issued_bk.html',{'course':b1})


def logoutstd_fun(request):
    return redirect('log')


