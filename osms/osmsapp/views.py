from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from osms.settings import EMAIL_HOST_USER
from django.http import Http404


def home(req):
    user = req.user
    if not(user.is_anonymous):
        if 'HOS' in str(user):
            supplier = False
            obj = HospitalDetail.objects.get(user=req.user)
            name = obj.name
            id = obj.unique_hospital_id
            p = HospitalOxygenCylinderStock.objects.all()
            if id in str(p):
                pass
            else:
                o = HospitalOxygenCylinderStock(unique_hospital_id = id,name= name)
                s = HospitalOxygenSupportedBedStock(unique_hospital_id = id,name =name )
                s.save()
                o.save()
            context = {'u':not(user.is_anonymous),'user':user,'hospital':obj,'supplier':supplier}
        else:
            supplier = True
            context = {'u':not(user.is_anonymous),'user':user,'hospital':None,'supplier':supplier}
    else:
        context = {'u':not(user.is_anonymous),'user':user}
        
    
    return render(req, 'home.html',context)

def test(req):
    return render(req, 'test1.html')

def info(req,id):
    user = req.user
    hospital = HospitalDetail.objects.get(unique_hospital_id=id)
    cylinder = HospitalOxygenCylinderStock.objects.get(unique_hospital_id = id)
    bed =HospitalOxygenSupportedBedStock.objects.get(unique_hospital_id=id)
    if 'HOS' in str(user):
        context = {'u':not(user.is_anonymous),'hospital':hospital,'bed':bed,'cylinder':cylinder,'user':user,'hos':True}
    else:
        context = {'u':not(user.is_anonymous),'hospital':hospital,'bed':bed,'cylinder':cylinder,'user':user,'supplier':True}
        
    return render(req, 'hospital_profile.html',context)

def oxygen_cylinder_update(req):
    user = req.user
    if user.is_authenticated:
        obj = HospitalDetail.objects.get(user=req.user).unique_hospital_id
        o = HospitalOxygenCylinderStock.objects.get(unique_hospital_id = obj)
        tot = o.total_oxygen_cylinders_stock
        use = o.oxygen_cylinders_in_use
        print(o.name)
        if req.method =='POST':
            tot_cylinders = req.POST.get('tot_cylinders')
            cylinders_incoming = req.POST.get('cylinders_incoming')
            cylinders_in_use = req.POST.get('cylinders_in_use')
            cylinders_taken = req.POST.get('cylinders_taken')
            if tot_cylinders:
                o.total_oxygen_cylinders_stock = int(tot_cylinders)
            if cylinders_incoming:
                o.incoming_oxygen_cylinders_stock = int(cylinders_incoming)
            if cylinders_in_use:
                o.oxygen_cylinders_in_use = int(cylinders_in_use)
            if cylinders_taken:
                o.oxygen_supported_beds_taken_for_use = int(cylinders_taken)
            o.save()
    else:
        raise Http404("Not authorized.")
    context = {"tot": tot,'use':use,'hospital':o}
    return render(req, 'oxy_cylinder.html',context)
def oxygen_bed_update(req):
    user = req.user
    if user.is_authenticated:
        obj = HospitalDetail.objects.get(user=req.user).unique_hospital_id
        o = HospitalOxygenSupportedBedStock.objects.get(unique_hospital_id = obj)
        tot = o.total_oxygen_supported_beds
        use = o.oxygen_supported_beds_in_use
        print(o.name)
        if req.method =='POST':
            tot_beds = req.POST.get('tot_beds')
            print(type(tot_beds))
            beds_incoming = req.POST.get('beds_incoming')
            beds_in_use = req.POST.get('beds_in_use')
            beds_taken = req.POST.get('beds_taken')
            beds_free = req.POST.get('beds_free')
            if tot_beds:
                o.total_oxygen_supported_beds = int(tot_beds)
            if beds_incoming:
                o.oxygen_supported_beds_incoming = int(beds_incoming)
            if beds_in_use:
                o.oxygen_supported_beds_in_use = int(beds_in_use)
            if beds_free:
                o.oxygen_supported_beds_free_for_use = int(beds_free)
            if beds_taken:
                o.oxygen_supported_beds_taken_for_use = int(beds_taken)
            o.save()
    else:
        raise Http404("Not Authorized")
        
    context = {"tot": tot,'use':use,'hospital':o,}
    return render(req, 'oxy_bed.html',context)


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    
    context = {}
    return render(request, 'login.html', context)

def Logout(req):
    logout(req)
    return redirect("home")


def hospital_details_update(req):
    user = req.user
    if user.is_authenticated:
        obj = HospitalDetail.objects.get(user=req.user)
        if req.method =='POST':
            name = req.POST.get('name')
            nurses = req.POST.get('nurses')
            doctors = req.POST.get('doctors')
            phone = req.POST.get('phone')
            location = req.POST.get('location')
            mail = req.POST.get('mail')
            if name:
                obj.name = name
            if nurses:
                obj.total_nurses = int(nurses)
            if doctors:
                obj.total_doctors = int(doctors)
            if phone:
                obj.contact_details = phone
            if location:
                obj.location = location
            if mail:
                obj.mail_id = mail
            obj.save()
            return redirect(f'/info/{obj.unique_hospital_id}')
    else:
        raise Http404("Not Authorized")
        
    context = {"hospital": obj}
    return render(req, 'hospital_profile_update.html', context)
    
def hospital_detail(req):
    return render(req, 'info.html')

def supplier_detail(req):
    obj = SupplierDetail.objects.get(user=req.user)
    hospital = HospitalDetail.objects.all()
    context = {'user':obj,'hospital':hospital,'u':req.user}
    return render(req, 'supplier_profile.html',context)

def supplier_details_update(req):
    user = req.user
    if user.is_authenticated:
        obj = SupplierDetail.objects.get(user=req.user)
        if req.method =='POST':
            name = req.POST.get('name')
            phone = req.POST.get('phone')
            location = req.POST.get('location')
            mail = req.POST.get('mail')
            if name:
                obj.name = name
            if phone:
                obj.contact_details = phone
            if location:
                obj.location_of_supply_center = location
            if mail:
                obj.mail_id = mail
            obj.save()
            return redirect('supplier_detail')
    else:
        raise Http404("Not Authorized")
        
    context = {"supplier": obj}
    return render(req, 'supplier_profile_update.html', context)
# def virudhunagar(req):
#     return render(req, 'virudhunagar.html')

# def Theni(req):
#     return render(req, 'Theni.html')

# def Theni_hospital1(req):
#     hospital1 = HospitalDetail.objects.get(unique_hospital_id="2")
#     hospital2 = HospitalOxygenCylinderStock.objects.get(unique_hospital_id="2")
#     hospital3 = HospitalOxygenSupportedBedStock.objects.get(unique_hospital_id="2")
#     return render(req, 'theni/hospital1.html', context={'hospital1':hospital1 , 'hospital2':hospital2 , 'hospital3':hospital3})

# def Theni_hospital2(req):
#     form = CreateSupplierDetailForm()
#     if req.method=='POST':
#         form = CreateSupplierDetailForm(req.POST)
#         if form.is_valid():
#             form.unique_supplier_id = '5'
#             form.save()
#             return redirect('home')
            
#     return render(req, 'theni/hospital2.html', context = {'form':form})

# def Theni_hospital3(req):
#     return render(req, 'theni/hospital3.html')

# def Theni_hospital4(req):
#     return render(req, 'theni/hospital4.html')

# def Theni_hospital5(req):
#     return render(req, 'theni/hospital5.html')

# def Theni_hospital6(req):
#     return render(req, 'theni/hospital1.html')

# def Theni_hospital7(req):
#     return render(req, 'theni/hospital1.html')

# def Theni_hospital8(req):
#     return render(req, 'theni/hospital1.html')

# def Theni_hospital9(req):
#     return render(req, 'theni/hospital3.html')

# def Theni_hospital10(req):
#     return render(req, 'theni/hospital4.html')

# def Theni_hospital11(req):
#     return render(req, 'theni/hospital5.html')

# def Theni_hospital12(req):
#     return render(req, 'theni/hospital1.html')

# def Theni_hospital13(req):
#     return render(req, 'theni/hospital1.html')

# def Theni_hospital14(req):
#     return render(req, 'theni/hospital1.html')


# def virudhunagar(req):
#     return render(req, 'virudhunagar.html')

# def virudhunagar(req):
#     return render(req, 'virudhunagar.html')



