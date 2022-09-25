from django.urls import path
from . import views,HodViews,StaffViews,StudentViews

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('doLogin/',views.doLogin,name='doLogin'),
    path('get_user_details/',views.get_user_details,name='get_user_details'),
    path('logout/',views.logout_user,name='logout'),
    # path('admin_home/',views.admin_home,name='admin_home'),
    # path('staff_home/',views.staff_home,name='staff_home'),
    # path('student_home/',views.student_home,name='student_home'),
]
