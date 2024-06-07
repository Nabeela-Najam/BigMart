from django.shortcuts import render, redirect
from backend.models import product_db, category_db
from webapp.models import contact_db, register_db, CartDb
from django.contrib import messages

# Create your views here.

def homepage(request):
    cat=category_db.objects.all()
    return render(request,"Home.html", {'cat':cat})

def aboutpage(request):
    cat = category_db.objects.all()
    return render(request,"About.html", {'cat':cat})

def contactpage(request):
    cat = category_db.objects.all()
    return render(request,"Contact.html",{'cat':cat})

def ourproductspage(request):
    pro=product_db.objects.all()
    cat = category_db.objects.all()
    return render(request,"OurProducts.html", {'products':pro, 'cat':cat})


def save_contact(request):
    if request.method == "POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        p=request.POST.get('phone')
        s=request.POST.get('subject')
        m=request.POST.get('message')

        obj1=contact_db(name=n, email=e, phone=p, subject=s, message=m)
        obj1.save()
        return redirect(contactpage)

def filtered_products(request, cat_name):
    data=product_db.objects.filter(pcategory=cat_name)
    return render(request,"Products_Filtered.html", {'data':data})

def single_product(request,proid):
    data=product_db.objects.get(id=proid)
    cat = category_db.objects.all()
    return render(request,"Single_Product.html", {'data':data, 'cat':cat})

def register(request):
    return render(request,"Register.html")

def save_register(request):
    if request.method == "POST":
        rna=request.POST.get('rname')
        rem=request.POST.get('remail')
        rpa=request.POST.get('rpassword')
        rcp = request.POST.get('cpassword')

        obj2=register_db(rname=rna, remail=rem, rpassword=rpa, cpassword=rcp)

        if register_db.objects.filter(rname=rna).exists():
            messages.warning(request,"Username already exists")
            return redirect(register)
        elif register_db.objects.filter(remail=rem).exists():
            messages.warning(request, "Email already exists")
            return redirect(register)
        else:
            obj2.save()
            messages.success(request,"Registered Successfully")
        return redirect(register)

def UserLogin(request):
    if request.method=="POST":
        us=request.POST.get('username')
        pwd=request.POST.get('password')
        if register_db.objects.filter(rname=us, rpassword=pwd).exists():
            request.session['rname']=us
            request.session['rpassword']=pwd

            messages.success(request,"Welcome.......!")
            return redirect(homepage)
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect(register)
    else:
        # messages.warning(request, "User not found...!")
        return redirect(register)

def UserLogout(request):
    del request.session['rname']
    del request.session['rpassword']
    messages.success(request, "Logout Successfully ...!")

    return redirect(homepage)

def save_cart(request):
    if request.method=="POST":
        un=request.POST.get('rname')
        pn=request.POST.get('pname')
        qu=request.POST.get('qty')
        tp=request.POST.get('tprice')

        obj8=CartDb(Username=un, Productname=pn, Quantity=qu, Totalprice=tp)
        obj8.save()
        messages.success(request, "Added To Cart ...!")
        return redirect(homepage)

def cart(request):
    data=CartDb.objects.filter(Username=request.session['rname'])
    # messages.success(request, "Logout Successfully ...!")
    total=0
    for d in data:
        total=total+d.Totalprice
    return render(request,"Cart.html",{'data': data, 'total':total})

def delete_item(request,pid):
    x=CartDb.objects.filter(id=pid)
    x.delete()
    messages.warning(request, "Removed From Cart")

    return redirect(cart)

def Userlogin(request):
    return render(request,"Userlogin.html")