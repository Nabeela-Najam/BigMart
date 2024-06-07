from django.shortcuts import render, redirect
from backend.models import category_db, product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from webapp.models import contact_db
# Create your views here.

def index(request):
    return render(request,"index.html")

def category(request):
    return render(request,"category.html")

def save_category(request):
    if request.method == "POST":
        cn=request.POST.get('cname')
        cd=request.POST.get('cdescription')
        cima=request.FILES['cimage']

        obj1=category_db(cname=cn, cdescription=cd, cimage=cima)
        obj1.save()
        messages.success(request,"Category Saved Successfully...!")
        return redirect(category)

def display_category(request):
    data=category_db.objects.all()
    return render(request,"display_category.html", {'data':data})

def edit_category(request, catid):
    data=category_db.objects.get(id=catid)
    return render(request,"edit_category.html", {'data':data})

def update_category(request, catid):
    if request.method == "POST":
        cn=request.POST.get('cname')
        cd=request.POST.get('cdescription')
        try:
            img=request.FILES['cimage']
            fs=FileSystemStorage()
            file=fs.save(img.name, img)

        except MultiValueDictKeyError:
            file=category_db.objects.get(id=catid).cimage
        category_db.objects.filter(id=catid).update(cname=cn, cdescription=cd, cimage=file)
        messages.success(request, "Category Updated Successfully...!")
        return redirect(display_category)

def delete_category(request, catid):
    x=category_db.objects.filter(id=catid)
    x.delete()
    messages.error(request, "Category Deleted Successfully...!")
    return redirect(display_category)

def admin_login(request):
    return render(request,"admin_login.html")

def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "Welcome...!")

                return redirect(index)
            else:
                messages.error(request, "Invalid Password...!")
                return redirect(admin_login)
        else:
            messages.warning(request, "User not found...!")
            return redirect(admin_login)

def Adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully ...!")

    return redirect(admin_login)

def product(request):
    data=category_db.objects.all()
    return render(request,"product.html", {'data':data})

def save_product(request):
    if request.method == "POST":
        pc=request.POST.get('pcategory')
        pn=request.POST.get('pname')
        pp=request.POST.get('pprice')
        pd=request.POST.get('pdescription')
        pima=request.FILES['pimage']

        obj2=product_db(pcategory=pc, pname=pn, pprice=pp, pdescription=pd, pimage=pima)
        obj2.save()
        messages.success(request, "Category Saved Successfully...!")
        return redirect(product)

def display_product(request):
    data = product_db.objects.all()
    return render(request,"display_product.html", {'data':data})

def edit_product(request,pid):
    data=product_db.objects.get(id=pid)
    cat = category_db.objects.all()
    return render(request,"edit_product.html", {'data':data, 'cat':cat})

def delete_product(request,pid):
    x=product_db.objects.filter(id=pid)
    x.delete()
    messages.error(request, "Product Deleted Successfully...!")

    return redirect(display_product)


def display_contact(request):
    data=contact_db.objects.all()
    return render(request,"display_contact.html", {'data':data})

def delete_contact(request,conid):
    x=contact_db.objects.filter(id=conid)
    x.delete()
    return redirect(display_contact)