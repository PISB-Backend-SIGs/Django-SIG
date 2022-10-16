from multiprocessing import context
from re import U
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages #import messages
from django.contrib.auth.models import User #for admin user database
from django.contrib.auth import authenticate,login,logout #for authentication system
from django.contrib.auth import login as log #for authentication system
from django.contrib.auth import logout as logt #for authentication system
from .models import Quiz,Credential,Uans,Ures
import re
# Create your views here.
#testuser1 123@prasad
#testuser2 Prasad@123
def index(request):
    # user=User.objects.get(username=request.user)
    # print(user)
    return render(request,'app/index.html',{'title':"Quizz"}) #,'user':user
def login(request):
    if request.method=="POST":
        usern=request.POST['uname']
        pasword=request.POST['pass']
        user =authenticate(request,username=usern,password=pasword)
        # print(usern)
        # print(pasword)
        # print(user)
        
        obj = User.objects.get(username=usern) #to get all data of one 
        
        if user is not None:
            log(request,user)
            cq=Credential.objects.get(user=request.user)
            # messages.success(request, "Message sent." )
            if cq.trys>0:
                return redirect('/result/')
            
            return redirect('/user_page/')
            # return render(request,'app/test.html',{'message':"Succesfuly Loged in",'display':obj})#,'dis':qui
        else:
            return render(request,'app/login.html',{'errors':"Invalid Credentials"})
    else:
        return render(request,'app/login.html')
def user_page(request):
    obj = User.objects.get(username=request.user)
    cq=Credential.objects.get(user=obj)
    return render(request,'app/test.html',{'message':"Succesfuly Loged in",'display':obj,'udisplay':cq})
def logout(request):
    logt(request)
    # return render(request,'app/index.html')
    return redirect('/index/')

def pass_question(request):
    context={}
    cq=Credential.objects.get(user=request.user)
    cq.crntque += 1
    cq.save()
    quiz_que = Quiz.objects.all()
    if Ures.objects.filter( user=request.user ,qid=cq.crntque).exists():
        obj=Ures.objects.get(user=request.user,qid=cq.crntque)
        # print(obj)  #it will print option 
        # print(obj.opts)  #it will print option 
        if obj.opts=="op1":
            context["op1"]=True
        if obj.opts=="op2":
            context["op2"]=True
        if obj.opts=="op3":
            context["op3"]=True
        if obj.opts=="op4":
            context["op4"]=True
    else:
        print("Not save it will save")
    
    
    if cq.crntque >1:
        context['prevs']=True
    if cq.crntque <10:
        context['buton']=True
    else:
        context['buton']=False
    ques = Quiz.objects.get(place = cq.crntque)
    # print(ques)
    context['question'] = ques
        
    return render(request,'app/quiz.html',context)
    
def cal(request):
    obj=User.objects.get(username=request.user)
    cq=Credential.objects.get(user=obj)
    ques = Quiz.objects.get(place = cq.crntque)
    for i in range(1,11):
        ques = Quiz.objects.get(place = i)
        obj=Ures.objects.get(user=request.user,qid=i)
        if ques.ans==obj.opts:
            cq.marks+=10
            cq.save()
        
    return redirect("/result")



def result(request):
    obj=User.objects.get(username=request.user)
    cq=Credential.objects.get(user=obj)
    # display by user module  display:obj
    # to display marks of user udisplay:cq
    cq.trys+=1
    cq.save()
    # messages.success(request, "Message sent.res" )
    return render(request,'app/test.html',{'display':obj,'udisplay':cq, 'flag':True})

def start(request):
    context={}
    if request.user.is_authenticated:
        if 'next' in request.POST:
            cq=Credential.objects.get(user=request.user)
            if request.POST.get('ans'):
                if Ures.objects.filter(user=request.user,qid=cq.crntque).exists():
                    obj=Ures.objects.get(user=request.user,qid=cq.crntque)
                    print(obj.opts)  #it will print option 
                    obj.opts=request.POST.get('ans')
                    obj.save()
                else:
                    obj=Ures(user=request.user,qid=cq.crntque,opts=request.POST.get('ans'))
                    obj.save()
            
            return redirect('/pass_question/')
        elif ('previous' in request.POST):
            cq=Credential.objects.get(user=request.user)
            cq.crntque -= 2
            cq.save()                
            return redirect('/pass_question/')
        elif ('submit' in request.POST):
            cq=Credential.objects.get(user=request.user)
            ques = Quiz.objects.get(place = cq.crntque)
            if request.POST.get('ans'):
                if Ures.objects.filter(user=request.user,qid=cq.crntque).exists():
                    obj=Ures.objects.get(user=request.user,qid=cq.crntque)
                    print(obj.opts)  #it will print option 
                    obj.opts=request.POST.get('ans')
                    obj.save()
                else:
                    obj=Ures(user=request.user,qid=cq.crntque,opts=request.POST.get('ans'))
                    obj.save()

            return redirect('/cal/')
        else:
            return redirect('/pass_question/')
    else:
        return render(request,'app/quiz.html')



#for signup 
def signup(request):
    error=[]
    ct=0
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
    
    

        #for authentication and errors
        if len(phone)!=10:
            error.append("Wrong phone number")
            ct+=1
        if  User.objects.filter(email=email).exists():
            error.append("Email is already register")
            ct+=1
        if Credential.objects.filter(phone_number=phone):
            error.append("Phone is already register")
            ct+=1
        if User.objects.filter(username=uname).exists() :
            error.append("Username is already register")
            ct+=1
        if (ct>=1):
            return render(request,'app/signup.html',{'errors':error})
   
        else:
            if pass1==pass2 :
                if len(pass1)>=8:
                    regex="(?=.*[a-z])(?=.*[A-Z])(?=.*[1-9])(?=.*[&@#$%])"
                    patt=re.search(regex,pass1)
                    if patt:
                        #for store in user database
                        user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,
                        password=pass1)
                        user.save()
                        #for store in userdatabase
                        data=Credential(user=user,phone_number=phone,crntque=0,marks=0,trys=0)
                        data.save()
                        uans=Uans(user=user)
                        uans.save()

                        return render(request,'app/index.html',{'message':"Succesfuly Account Created"})                    

                    else :

                        passmessage="Password should be atleast 8 digit \n It must contain atlest 1 uppercase character \n atleast 1 lowercase character \n atlest one special character"
                        return render(request,'app/signup.html',{'passmessage':passmessage})
                else :
                    # print ("password should be greater than 7 character")
                    return render(request,'app/signup.html',{'passmessage':"password should be greater than 7 character"})
                
            else:
                return render(request,'app/signup.html',{'passmessage':"Passwords are not same"})
                
    else:
        return render(request,'app/signup.html')
