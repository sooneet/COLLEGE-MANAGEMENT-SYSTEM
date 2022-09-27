from django.urls import path
from . import views,HodViews,StaffViews,StudentViews

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('doLogin/',views.doLogin,name='doLogin'),
    path('get_user_details/',views.get_user_details,name='get_user_details'),
    path('logout/',views.logout_user,name='logout'),
    path('admin_home/',HodViews.admin_home,name='admin_home'),
    path('manage_staff/',HodViews.manage_staff,name='manage_staff'),
    path('add_staff/',HodViews.add_staff,name='add_staff'),
    path('add_staff_save/',HodViews.add_staff_save,name='add_staff_save'),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name='delete_staff'),
    path('edit_staff/<staff_id>/',HodViews.edit_staff,name='edit_staff'),
    path('edit_staff_save/',HodViews.edit_staff_save,name='edit_staff_save'),
    path('add_student/',HodViews.add_student,name='add_student'),
    path('add_student_save/',HodViews.add_student_save,name='add_student_save'),
    path('add_course/',HodViews.add_course,name='add_course'),
    path('add_course_save/',HodViews.add_course_save,name='add_course_save'),
    path('manage_course/',HodViews.manage_course,name='manage_course'),
    path('edit_course/<course_id>/',HodViews.edit_course,name='edit_course'),
    path('delete_course/<course_id>/',HodViews.delete_course,name='delete_course'),
    path('edit_course_save/',HodViews.edit_course_save,name='edit_course_save'),
    # path('add_session/',HodViews.add_session,name='add_session'),
    # path('add_session_save/',HodViews.add_session_save,name='add_session_save'),

    #staff
    path('staff_home/',StaffViews.staff_home,name='staff_home'),

    #student
    path('student_home/',StudentViews.student_home,name='student_home'),

]
