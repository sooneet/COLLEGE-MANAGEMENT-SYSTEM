from django.shortcuts import render,redirect
from django.contrib import messages
from . models import CustomUser, Staffs





def admin_home(request):
    return render(request, "hod_template/home_content.html", {})

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