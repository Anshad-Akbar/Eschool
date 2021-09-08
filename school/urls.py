from django.urls import path,include
from.import views

urlpatterns = [
    path('login',views.LoginFn,name='login'),
    path('register',views.registerFn,name='register'),
    path('dashbord',views.dashbordFn,name='dashbord'),
    path('student_home',views.student_dashbordFn,name='student_home'),
    path('student_details',views.detailsFn,name='student_details'),
    path('edit/<int:id>',views.editFn,name='edit'),
    path('update/<int:id>',views.updateFn,name='update'),
    path('active',views.activeFn,name='active'),
    path('inactive',views.inactiveFn,name='inactive'),
    path('inactivate/<int:id>',views.inactivateFn,name='inactivate'),
    path('activate/<int:id>',views.activateFn,name='activate'),

 


]