from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from blog.models import Post
# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def contact(request):
    if request.method== 'POST':
        name= request.POST['name']        
        email= request.POST['email']  
        subject= request.POST['subject']    
        message= request.POST['content'] 
        query= request.POST['query'] 
        #Check for Logged In user
        if request.user.id == None :
            messages.error(request," Your are not a Valid User. Please Log In! ")
            return render(request,'app1/contact.html')
        #check for erroneous inputs
        if len(name)<2 or len(email)<3 or len(email)<10 or len(message)<4:
            messages.error(request,"Please fill the form correctly")
        else :
            messages.success(request," Your Query has been received by us. We'll connect with you soon! ")
        contact = Contact(name=name, email=email, subject=subject, message=message,query=query)
        contact.save()
    return render(request,'app1/contact.html')
def queries(request):
    if request.user.id != None :
        allQueries= Contact.objects.all()
        context={'allQueries':allQueries}
        return render(request,'app1/queries.html',context)
    else :
        messages.error(request," Your are not a Valid User. Please Log In! ")
        return redirect('home')
        
# Authentication APIs
def handleSignup(request):
    if request.method == "POST":
        #get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        dob = request.POST['date']
        gender= request.POST['gender']

        #check for eroneous inputs
        if len(username)>10 :
            messages.error(request," Username must be under 10 character!")
            return redirect('home')
        if len(email)>25:
            messages.error(request," Email should be under 20 characters!")
            return redirect('home')
        if not username.isalnum():
            messages.error(request," Username should only contain alphanumeric characters!")
            return redirect('home')

        if(pass1 != pass2):
            messages.error(request,"Your password doesn't match!")
            return redirect('home')
        
        #create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.save()
        messages.success(request,"Your Account has been successfully created!")
        return redirect('home')
    else:
        return HttpResponse('404- Not Found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpass)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('home')


    return HttpResponse("404 - Not found")

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out!")
    return redirect('home')
