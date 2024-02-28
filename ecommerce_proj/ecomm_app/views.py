from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from.models import *


 


# Create your views here.
def register(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       uname = request.POST['user_name']
       email = request.POST['email']
       password = request.POST['password1']
       con_password = request.POST['password2']
       if password == con_password:
           if User.objects.filter(username=uname).exists():
               messages.info(request,'username already taken')
               return redirect('registration')
           elif User.objects.filter(first_name=first_name).exists():
               messages.info(request,'Name already taken')
               return redirect('registration')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'email already exists')
               return redirect('registration')
           else:
               reg_user =User.objects.create_user(
                   username = uname,
                   first_name = first_name,
                   email = email,
                   password = password
               )
               reg_user.save()
               messages.success(request,'Registration successful')
               return redirect('login')
       else:
           messages.error(request,'Passwords do not match')
           return redirect('registration')   
       

    return render (request,'register.html')
   

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        pass1 = request.POST.get('password1')
        we = authenticate(request,username=uname,password=pass1)

        if we is not None:
           auth_login(request,we)
           return redirect("index")
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')

    
    return render(request,'login.html')


def index(request):
    View =Product.objects.all()
    context={
    'view':View
}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def single(request,pk):
    View =Product.objects.get(pk=pk)
    context={
        'view':View
        }
    return render(request,'single_product.html',context)

def cart(request,pk):
    admin = request.user
    cart_pro = Product.objects.get(pk=pk)
    cart_product= CartItem(product=cart_pro,user=admin)
    cart_product.save()
    return redirect('view_cart')


def view_cart(request):
    admin= request.user
    cart_items = CartItem.objects.filter(user=admin)

    context = {
        'cart_items':cart_items
    }
    return render(request,'cart_1.html',context)


def shop(request):
    return render(request,'shop.html')

def services(request):
    
     return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def thankyou(request):
    return render(request,'thankyou.html')



   
