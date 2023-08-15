from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from django.shortcuts import render, redirect 
from edu.forms import *
from django.shortcuts import render,redirect,get_object_or_404,redirect
from edu.models import *

# Create your views here.
def handler_not_found(request,exception):
    return render(request, "not_found.html")

def page_admin(request):  
    return render(request,"page_admin.html")

def product_delete_view(request,id):
     obj = get_object_or_404(teacherupload, id=id)
     if request.method =="POST":
        obj.delete()
     return redirect("../../")
     context={
         "object":obj
     }
     return render(request, "product_delete.html", context)





def detail(request,id):
    obj=get_object_or_404(showcontent,pk=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('index')
    return render(request,"detail.html",{"obj":obj})







def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect("/selectsubject")
    else:
        form =UserCreationForm()
    return render (request,'registration/signup.html',{'form':form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            reg_class = form.cleaned_data.get('reg_class')
            user= authenticate(username=username, password=password, reg_class=reg_class)
            if user is not None:
                login(request, user)
                messages.info(request,"you are logged in as {username}.")
                return redirect("/selectsubject")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password")
    form = AuthenticationForm()
    return render(request,'registration/login.html',{'login_form':form})

# @login_required(login_url='/login_request/')
def logout_user(request):
    logout(request)
    return render(request,'logout.html')

def success(request):
    return render(request, 'success.html', {})

def remove(request):
    obj=teacherupload.objects.filter(subject=syllabus_class,Class=syllabus_term)
    return render(request, 'onedelete.html', {"obj":obj})





def deletedetail(request):
    obj=teacherupload.objects.all()
    return render(request, 'deletedetail.html', {"obj":obj})

def bfordelete(request):
    return render(request, 'bfordelete.html', {"obj":obj})


def selectSubject(request):
    subjectform = SelectSubjectForm(request.POST or None)
    if (request.method =="POST"):
        subjectform = SelectSubjectForm(request.POST or None)
        if subjectform.is_valid:
            subjectname = subjectform['subjectname'].value()
            classname= subjectform['classname'].value()
            print(classname,subjectname)
            return redirect("selectthisusbject/"+subjectname+"/"+classname)
    subjectform = SelectSubjectForm()
    data={"form":subjectform}
    return render(request,"selectSubject.html",data)


def delete_syllabus(request, id):
     obj=get_object_or_404(Syllabus,id=id)
     if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/selectsyllabus")
       
     context={
         "objects":obj
     }
     return render(request,"syllabusdelete.html",context) 

def ok_delete(request):
    return render(request,"/showcontent")

def delete_comment(request,id):
    obj=get_object_or_404(add_comments,id=id)
    if request.method == "POST":
       obj.delete()
       return HttpResponse("item successfully deleted")
    else:
        
        context={
            "objects":obj
        }
    return render(request,"bfordelete.html",context) 

def update_syllabus(request, id):
     obj=Syllabus.objects.get(id=id)
     form=SyllabusUploadForm(request.POST or None, instance=obj)
     if form.is_valid():
        form.save()
        return redirect("/selectsyllabus")
    
     return render(request,"update_syllabus.html",{"objects":obj,"form":form}) 

def schedule_upload(request):
    if request.method =='POST':
        form=eventform(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/event_view")
    else:
        form=eventform
    return render(request,"schedule.html",{"form":form})

def schedule_view(request):
    obj=schedule.objects.all()
    return render(request,"schedule_view.html",{"obj":obj})

def lectureupdate(request, id):
     obj=teacherupload.objects.get(id=id)
     form=teacheruploadForm(request.POST or None, instance=obj)
     if form.is_valid():
        form.save()
        return redirect("/selectsubject")
    
     return render(request,"update_syllabus.html",{"objects":obj,"form":form})    

def update_user(request, id):
     obj=User.objects.get(id=id)
     form=SignUpForm(request.POST or None, instance=obj)
     if form.is_valid():
        form.save()
        return redirect("/selectSubject")
    
     return render(request,"update_user.html",{"objects":obj,"form":form})    


def delete(request,id):
    obj=get_object_or_404(teacherupload,pk=id)
    subjectform = SelectSubjectForm(request.POST or None)
    if request.method == "POST":
        obj.delete()
        subjectname = subjectform['subjectname'].value()
        classname= subjectform['classname'].value()
        print(classname,subjectname)
        return redirect("/selectsyllabus")
    else:
        redirect("/selectsyllabus")
    return render(request,"bfordelete.html",{"obj":obj})





def selectsyllabus(request):
    syllabusform = SyllabusForm(request.POST or None)
    if (request.method =="POST"):
        syllabusform = SyllabusForm(request.POST or None)
        if syllabusform.is_valid:
            syllabus_class = syllabusform['syllabus_class'].value()
            syllabus_subject = syllabusform['syllabus_subject'].value()
            return redirect("seesyllabus/"+syllabus_class+"/"+syllabus_subject)
    syllabusform = SyllabusForm()
    data={"form":syllabusform}
    return render(request,"selectsyllabus.html",data)
    
def seesyllabus(request,syllabus_class,syllabus_subject):
    '''return HttpResponse(syllabus_class)'''
    data =Syllabus.objects.filter(syllabus_class=syllabus_class,syllabus_subject=syllabus_subject)
    xdata={"data":data}   


    return render(request ,"seesyllabus.html",xdata)







def selectThisSubject(request,subjectname,classname):
    '''return HttpResponse(subjectname)'''
    if(subjectname=="english","mathematics","physics","chemistry","biology","economics","accounts","government","literature","geography","futher-maths"):
        data =teacherupload.objects.filter(subject=subjectname,Class=classname)
        xdata={"data":data}
    for i in data:
            print(i.topic,"")
    return render(request ,"showtopics.html",xdata)

def showcontent(request,slug):
    '''return HttpResponse(subjectname)'''
    post=get_object_or_404(teacherupload, slug=slug)
    comments=post.add_comments.filter(active=True, parent__isnull=True )
    new_comment=None
    data =teacherupload.objects.filter(slug=slug)

    if request.method=='POST':
        form=Add_CommentsForm(request.POST,request.FILES)
        if form.is_valid():
            parent_obj =None
            try:
                parent_id= int(request.POST.get('parent_id'))
            except:
                parent_id=None
            if parent_id:
                parent_obj =add_comments.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment=form.save(commit=False)
                    replay_comment.parent=parent_obj 

            new_comment =form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            return HttpResponseRedirect(".")
    else:
        form=Add_CommentsForm() 
    
    xdata={"data":data,
            "post":post,
            "comments":comments,
            "new_comment":new_comment,
            "form":form,
            }


    return render(request ,"showcontent.html",xdata)









def syllabus(request,syllabus_class,syllabus_term):
    if(syllabus_class=="JSS1"):
        datas =Syllabus.objects.filter(subject=syllabus_class,Class=syllabus_term)
        xdata={"datas":datas}    
    post=get_object_or_404(teacherupload, slug=slug)
    syllabuss=Syllabus.objects.filter(post=post)
    if request.method=='POST':
        syllabus_form=SyllabusForm(data=request.POST or None)
        if syllabus_form.is_valid():
            body = request.POST.get("scheme","textbooks","syllabus_class","syllabus_term")
            syllabus = Syllabus.objects.create(scheme=scheme, textbooks=textbooks)
            syllabus.save()
            
    else:
        syllabus_form=SyllabusForm()

    xdata={ "post":post,
            "datas":datas,
            "syllabuss":syllabuss,
            "syllabus_form":syllabus_form,
            }

    return render(request ,"syllabus.html",xdata)

def syllabusupload(request):    
    if request.method =='POST':
        form=SyllabusUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SyllabusUploadForm()
    return render(request, 'syllabusupload.html',{'form':form})
    
def upload(request):    
    if request.method =='POST':
        form=teacheruploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = teacheruploadForm()
    return render(request, 'upload.html',{'form':form})



