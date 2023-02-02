from django.urls import path

from Libraryapp import views

urlpatterns=[
    path('',views.log_fun,name='log'),
    path('logdata',views.logdata_fun),
    path('adminreg',views.admin_reg_fun,name='admin'),
    path('studentreg',views.student_reg_fun,name='student'),
    path('regdata',views.admin_regdata_fun),
    path('sregdata', views.student_regdata_fun),
    path('adminhome',views.admin_home_fun,name='ahome'),


    path('home',views.home_fun,name='home'),
    path('displaybook',views.displaybook_fun,name='display'),
    path('add_book',views.addbook_fun,name='add'),
    path('readdata',views.readbookdata_fun),

    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out'),


    path('assigndata',views.assign_fun,name='assign'),
    path('readassigndata',views.readassigndata_fun,name='get'),
    path('sreaddata',views.assignbookdata_fun,name='issued'),


    path('issuedata',views.issuebook_fun,name='issue'),

    path('update2/<int:id>',views.update2_fun,name='update2'),
    path('del2/<int:id>',views.delete2_fun,name='del2'),

    #student urls:

    path('studenthome',views.student_home_fun,name='shome'),
    path('profile',views.profile_fun,name='profile'),
    path('updatepro/<int:id>',views.updatepro_fun,name='updatepro'),
    path('issuedbk',views.issuebkdet_fun,name='issuedbook'),
    path('logoutstd',views.logoutstd_fun,name='logoutstd'),







]