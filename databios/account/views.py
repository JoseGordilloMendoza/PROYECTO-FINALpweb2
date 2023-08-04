from almacen.views import homeView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from almacen.models import ShoppingCar, itemCar, Product
from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(email):
    subject = 'Verificación de correo'
    message = 'Gracias por registrarte. Tu cuenta fue creada con exito'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')  

        else:
            messages.error(request, 'Credenciales inválidas')
            return redirect('/login/')

    else:
        return render(request, 'login.html')  

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                send_verification_email(email)
                return redirect('/login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('/register')
        return redirect(homeView)
        
    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect(homeView)    