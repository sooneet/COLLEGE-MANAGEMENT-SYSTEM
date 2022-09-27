from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Courses, CustomUser, SessionYearModel, Staffs, Student
from . forms import AddStudentForm, EditStudentForm
from django.core.files.storage import FileSystemStorage


def admin_home(request):
    return render(request, "hod_template/home_content.html", {})

#staff
def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        'staffs':staffs
    }
    return render(request,'hod_template/manage_staff_template.html',context)

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method != "POST":
        messages.error(request,'Invalid Method')
    else:
        first_name = request.POST.get('first_name')   
        last_name = request.POST.get('last_name')   
        email = request.POST.get('email')   
        password = request.POST.get('password')   
        address = request.POST.get('address')   
        username = request.POST.get('username')   

        try:
            user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,
                                                  email=email,password=password,
                                                  username=username,user_type=2)
            user.staffs.address = address
            user.save()   
            messages.success(request,'Staff Added Successfully!')    
            return redirect('add_staff')                                           
        except:
            messages.success(request,'Failed to Add Staff!')    
            return redirect('add_staff')   
        
def edit_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    context = {
        'staff':staff
    }
    return render(request,"hod_template/edit_staff_template.html",context)

def edit_staff_save(request):
    if request.method != "POST":
        messages.error(request,'Invalid Method')
    else:
        staff_id = request.POST.get('staff_id')   
        first_name = request.POST.get('first_name')   
        last_name = request.POST.get('last_name')   
        email = request.POST.get('email')   
        # password = request.POST.get('password')   
        address = request.POST.get('address')   
        username = request.POST.get('username')   

        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            # user.password = password
            user.username = username
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()   
            messages.success(request,'Staff Updated Successfully!')    
            return redirect('/edit_staff/'+staff_id)                                           
        except:
            messages.success(request,'Failed to Update Staff!')    
            return redirect('/edit_staff/'+staff_id)    

def delete_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request,'Staff deleted Successfully!')    
        return redirect('manage_staff')                                           
    except:
        messages.success(request,'Failed to delete Staff!')    
        return redirect('manage_staff')      

#student
def add_student(request):
    form = AddStudentForm()
    context = {
        'form':form
    }
    return render(request,"hod_template/add_student_template.html",context)

# def add_student_save(request):
    if request.method != "POST":
        messages.error(request,'Invalid Method')
        return redirect('add_student')
    else:
        form = AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = request.cleaned_data('first_name')   
            last_name = request.cleaned_data('last_name')   
            email = request.cleaned_data('email')   
            password = request.cleaned_data('password')    
            username = request.cleaned_data('username')   
            address = request.cleaned_data('address')  
            course_id = request.cleaned_data('course_id')   
            # session_year_id = request.cleaned_data('session_year_id')  
            gender = request.cleaned_data('gender') 

            if len(request.FILES) !=0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name,profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic = None
        try:
            user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,
                                                  email=email,password=password,
                                                  username=username,user_type=3)
            user.students.address = address
            user.students.gender = gender
            user.students.profile_pic = profile_pic

            course_obj = Courses.objects.get(id=course_id)
            # session_year_obj = SessionYearModel.objects.get(id=session_year_id)

            user.save()   
            messages.success(request,'Student Added Successfully!')    
            return redirect('add_student')                                           
        except:
            messages.success(request,'Failed to Add Staff!')    
            return redirect('add_student') 

def add_course(request):
    return render(request,"hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        messages.error(request,'Invalid Method')
        return redirect('add_course')
    else:
        course = request.POST.get('course')   
        try:
            course_model = Courses(course_name=course)
            course_model.save()   
            messages.success(request,'Course Added Successfully!')    
            return redirect('add_course')                                           
        except:
            messages.success(request,'Failed to Add Course!')    
            return redirect('add_course')       

def manage_course(request):
    courses = Courses.objects.all()
    context = {
        'courses':courses,
    }
    return render(request,'hod_template/manage_course_template.html',context)

def edit_course(request,course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        'course':course,
        'course_id':course_id
    }
    return render(request,'hod_template/edit_course_template.html',context)

def edit_course_save(request):
    if request.method != "POST":
        HTTPResponse('Invalid Method')
    else:
        course_name = request.POST.get('course')    
        course_id = request.POST.get('course_id')    

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success(request,'Course Updated Successfully.')
            return redirect('/edit_course/'+course_id)
        except:
            messages.error(request,'Failed to Update Course.')
            return redirect('/edit_course/'+course_id)

def delete_course(request,course_id):
    course = Courses.objects.get(id=course_id)
    
    try:
        course.delete()
        messages.success(request,'Course deleted Successfully!')    
        return redirect('manage_course')                                           
    except:
        messages.success(request,'Failed to delete Course!')    
        return redirect('manage_course')    


# def add_session(request):
#     return render(request,"hod_template/add_session_template.html")    

# def add_session_save(request):
#     if request.method != "POST":
#         messages.error(request,'Invalid Method')
#         return redirect('add_course')
#     else:
#         session_start_year = request.POST.get('session_start_year')   
#         session_end_year = request.POST.get('session_end_year')   
#         try:
#             sessionyear = Courses(session_start_year=session_start_year,session_end_year=session_end_year)
#             sessionyear.save()   
#             messages.success(request,'Course Added Successfully!')    
#             return redirect('add_session')                                           
#         except:
#             messages.success(request,'Failed to Add session!')    
#             return redirect('add_session')       
