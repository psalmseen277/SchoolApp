from django import forms
from django.db import transaction
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from edu.models import SelectSubject,Comment,Syllabus,teacherupload,add_comments,Login,schedule
from .models import *
from django.forms import ModelForm, TextInput, EmailInput
# ,Employee,Customer

# create forms here  
CLASS=(
        ('JSS1','JSS1'),
        ('JSS2','JSS2'),
        ('JSS3','JSS3'),
        ('SSS1','SSS1'),
        ('SSS2','SSS2'),
        ('SSS3','SSS3')
    )

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=30,required=False,help_text='optional')
    last_name=forms.CharField(max_length=30,required=False,help_text='optional')
    reg_class=forms.ChoiceField(choices=CLASS) 

    class Meta:
        model=User
        fields="__all__"
        help_texts={
            "username":None,
        }



class SelectSubjectForm(forms.ModelForm):
     class Meta:
        model = SelectSubject
        fields="__all__"
        widgets = {
            'subjectname': forms.Select(attrs={'class': 'form-control','placeholder':'Select Subject'}),
            'classname': forms.Select(attrs={'class': 'form-control','placeholder':'Select Class'})
          }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class commentuploadForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= "__all__"

class teacheruploadForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = teacherupload
        fields= "__all__"



# this is invalid
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=  ['body']
        labels={
            'body':(''),
        }
        widgets={
            'body': forms.TextInput(),
        } 
# invalidstops here


class SyllabusForm(forms.ModelForm):
    class Meta:  
        model = Syllabus
        fields = ("syllabus_class","syllabus_subject")
        widgets = {
                'syllabus_class': forms.Select(attrs={'class': 'form-control','placeholder':'Select Subject'}),
                'syllabus_subject': forms.Select(attrs={'class': 'form-control','placeholder':'Select Class'})
          }


class SyllabusUploadForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = "__all__"
        widgets = {
            'syllabus_class': forms.Select(attrs={'class': 'form-control','placeholder':'Select Subject'}),
            'syllabus_subject': forms.Select(attrs={'class': 'form-control','placeholder':'Select Class'})
          }



class Add_CommentsForm(forms.ModelForm):
    class Meta:
        model = add_comments
        fields = ("name","body")

# class eventform(forms.Form):
#     event_name=models.CharField(max_length=240)
#     date=forms.DateTimeField(widget=NumberInput(attrs={'type': 'date'}))
#     description=forms.CharField(widget=forms.Textarea(attrs={'rows':6}))
#     link=models.CharField(max_length=120)
class eventform(forms.ModelForm):
    class Meta:
        model = schedule
        fields = "__all__"
        widgets = {
            
            'date': forms.DateTimeInput(attrs={'class': 'form-control','placeholder':'Date'}),
            'event': forms.TextInput(attrs={'class': 'form-control','placeholder':'Event'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Content'}),
            'link': forms.TextInput(attrs={'class': 'form-control','placeholder':'Link or Venue'})
          }  