
from http.client import HTTPResponse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login as lk,logout,update_session_auth_hash
from .forms import EditProfile,EditAdminProfile,post_blog
from django.contrib.auth.models import User
from .models import Blogs
from newsapi import NewsApiClient
# Create your views here.
def signup(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.set_level(request,5)
            messages.info(request,"congratulations your account is created")
            fm=UserCreationForm()
            return HttpResponseRedirect("/home/login/")
    else:
        fm=UserCreationForm()
    return render(request,"home.html",{"res":fm})

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home/profile")
    if request.method=="POST":
        fm=AuthenticationForm(request,data=request.POST)
        if fm.is_valid():
            usernm=fm.cleaned_data["username"]
            paaswrd=fm.cleaned_data["password"]
            print("username is ",usernm)
            print("passwrd is ",paaswrd)
            user=authenticate(username=usernm,password=paaswrd)
            print("user is ",user)
            if user is not None:
                lk(request,user)
                messages.set_level(request,5)
                messages.info(request,"welcome to profile page")
                return HttpResponseRedirect("/home/profile/")
    else:
        fm=AuthenticationForm()
    return render(request,"login.html",{"res":fm})

def guest_login(request):
    request.session['active']=True
    return HttpResponseRedirect("/home/profile/")

def profile(request):
    a=request.session.get("active",False)
    print("a is ",a)
    if not a:
        messages.info(request,"session has expired...")
        return HttpResponseRedirect("/home/login/")
    if request.user.is_authenticated:
        blog_posted=Blogs.objects.filter(user=request.user.id).count()
        if request.method=="POST":
            if request.user.is_superuser:
                fm=EditAdminProfile(request.POST,instance=request.user)
                user=User.objects.all()
                fm=EditProfile(instance=request.user)
            else:
                print("hii 3")
                fm=EditProfile(request.POST,instance=request.user)
                print("fm post is ",fm)
                user=False
            if fm.is_valid():
                fm.save()
                messages.success(request,"record updated")
        else:
            if request.user.is_superuser:
                fm=EditAdminProfile(instance=request.user)
                user=User.objects.all()
            else:
                print("hiii2")
                fm=EditProfile(instance=request.user)
                print("fm is ",fm)
                user=False
        return render(request,"profile.html",{"name":request.user,"form":fm,"active_user":user,"blog_posted":blog_posted})
    else:
        return render(request,"profile.html")

def log__out(request):
    logout(request)
    return HttpResponseRedirect("/home/login/")


#change password with old password
def change_pass_with_old(request):
    if not request.user.is_authenticated:
        messages.success(request,"mere bhai login kr phle")
        return HttpResponseRedirect("/home/login")
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,"mubark ho bhai ji password reset ho gya hai!!")
            return HttpResponseRedirect("/home/profile/")
    else:
        fm=PasswordChangeForm(request.user)
    return render(request,"changepass.html",{"form":fm})


#change password without old password
def change_pass_without_old(request):
    if not request.user.is_authenticated:
        messages.success(request,"mere bhai login kr phle")
        return HttpResponseRedirect("/home/login")
    if request.method=="POST":
        fm=SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,"mubark ho bhai ji password reset ho gya hai!!")
            return HttpResponseRedirect("/home/profile/")
    else:
        fm=SetPasswordForm(request.user)
    return render(request,"changpass1.html",{"form":fm})


def user_details(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm=EditAdminProfile(instance=pi)
        return render(request,"profile.html",{"form":fm,"user":None})
    else:
        messages.info(request,"phle login kr bhai")
        return HttpResponseRedirect("/home/login/")

def public_blog(request):
    blog_data=Blogs.objects.all()
    return render(request,"blog.html",{"form":blog_data})

def delete_blog(request,id):
    res=Blogs.objects.filter(id=id).delete()
    messages.info(request,"blog deleted sucessfully!")
    return HttpResponseRedirect("/home/public_blog/")

def create_post(request,id=None):
    if request.method=="POST":
        blog=post_blog(request.POST)
        if blog.is_valid():
            title=blog.cleaned_data["title"]
            category=blog.cleaned_data["category"]
            description=blog.cleaned_data["description"]
            u_id=User.objects.get(pk=request.user.id)
            blog_temp=Blogs(title=title,category=category,description=description,user=u_id).save()
            messages.info(request,"blog posted sucessfully!")
            print("title is ",title)
            print("category is ",category)
            print("description is ",description)
            print("user is ",u_id)
            return HttpResponseRedirect("/home/create_post/")
    else:
        if id==None:
            print("yes")
        blog=post_blog()
    return render(request,"create_post.html",{"form":post_blog})

def edit_post(request,id):
    if request.method=="POST":
        blog=post_blog(request.POST)
        if blog.is_valid():
            title=blog.cleaned_data["title"]
            category=blog.cleaned_data["category"]
            description=blog.cleaned_data["description"]
            u_id=User.objects.get(pk=request.user.id)
            blog_temp=Blogs(id=id,title=title,category=category,description=description,user=u_id).save()
            messages.info(request,"blog updated sucessfully!")
            print("title is ",title)
            print("category is ",category)
            print("description is ",description)
            print("user is ",u_id)
            return HttpResponseRedirect("/home/create_post/")
    else:
        blog_data=Blogs.objects.filter(id=id).values()
        print("blog_data ",blog_data)
        blog=post_blog(initial={"title":blog_data[0]["title"],"category":blog_data[0]["category"],"description":blog_data[0]["description"]})
    return render(request,"editpost.html",{"form":blog,"id":id})


def news(request):
    # Init
    newsapi = NewsApiClient(api_key='d06eedd0fdd1496b9dc58725d5249fbf')

    #https://newsapi.org/v2/everything?q=Apple&from=2022-12-03&sortBy=popularity&apiKey=d06eedd0fdd1496b9dc58725d5249fbf
    # /v2/everything
    all_articles = newsapi.get_everything(q='programming languages',
                                          from_param='2022-12-01',
                                          to='2022-12-03',
                                          language='en',
                                          sort_by='relevancy',
                                          page=1,
                                          page_size=5)

    # /v2/top-headlines/sources
    print("----------sources are--------------")
    for i in all_articles['articles']:
        print("title:\n",i["title"])
        print("url:\n",i['url'])
    sources = newsapi.get_sources()
    print("------------------------------------")
    return render(request,"news.html",{"form":all_articles['articles']})