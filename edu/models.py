from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import *
from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput,EmailInput
from django.db.models.deletion import CASCADE
from django.db.models.base import Model


# Create your models here.
CLASS=[
        ('JSS1','JSS1'),
        ('JSS2','JSS2'),
        ('JSS3','JSS3'),
        ('SSS1','SSS1'),
        ('SSS2','SSS2'),
        ('SSS3','SSS3')
]
TERM=[
        ('1ST TERM','1ST TERM'),
        ('2ND TERM','2ND TERM'),
        ('3RD TERM','3RD TERM')
]
SUBJECTS=[
    ('mathematics','mathematics'),
    ('english','english'),
    ('physics','physics'),
    ('chemistry','chemistry'),
    ('biology','biology'),
    ('economics','economics'),
    ('accounts','accounts'),
    ('government','government'),
    ('literature','literature'),
    ('geography','geography'),
    ('futher-maths','futher-maths')
]





class teacherupload(models.Model):
        subject=models.CharField(max_length=60,choices=SUBJECTS)
        Class=models.CharField(max_length=60,choices=CLASS)
        topic=models.CharField(max_length=120)
        content=RichTextUploadingField()
        slug=models.SlugField('Add subject abbreviation, pick three letter from topic, add class and term and  date e.g mtsalgjss11')
        term=models.TextField(max_length=20,choices=TERM)
        audio=models.FileField(upload_to="audio",default="media/audio/aud1", null='' ,blank='True')
        videos=models.FileField(upload_to="video", default="media/video/vid1",null='' ,blank='True')
        created_on=models.DateTimeField(default=datetime.now)






class add_comments(models.Model):
        post=models.ForeignKey(teacherupload,on_delete=models.CASCADE,related_name='add_comments')
        name=models.CharField(max_length=80,default="")
        body=RichTextUploadingField()
        video=models.FileField(upload_to="video", default="")
        sound=models.FileField(upload_to="sound", default="")
        created_on=models.DateTimeField(auto_now_add=True)
        active=models.BooleanField(default=True)
        # reply=models.ForeignKey('add_comments',on_delete=models.CASCADE,related_name='reply', blank=True,null=True)
        parent=models.ForeignKey('add_comments', null=True , blank=True , on_delete=models.CASCADE, related_name='replies')

        class Meta:
                ordering=['-created_on']
        def __str__(self):
                return str(self.name)  +  'comment' +  str(self.body)
        @property
        def children(self):
                return add_comments.objects.filter(parent=self).reverse()

        @property
        def is_parent(self):
                if self.parent is None:
                        return True
                return False   
        

# class add_comments(models.Model):
#         post=models.ForeignKey(teacherupload,on_delete=models.CASCADE,related_name='add_comments')
#         name=models.CharField(max_length=80)
#         body=models.TextField()
#         video=models.FileField(upload_to="video", default="")
#         sound=models.FileField(upload_to="sound", default="")
#         created_on=models.DateTimeField(auto_now_add=True)
#         active=models.BooleanField(default=True)
#         reply=models.ForeignKey('add_comments',null=True,related_name='replies', blank=True,on_delete=models.CASCADE)
#         class Meta:
#                 ordering=['created_on']

#         def __str__(self):
#                 return 'comment {} by {}'.format(self.body,self.name)

class SelectSubject(models.Model):
       subjectname=models.CharField("Select Subject",choices=SUBJECTS,max_length=120)
       classname=models.CharField("Select Class",choices=CLASS,max_length=120)

class Comment(models.Model):
        # user=models.ForeignKey(user,on_delete=models.CASCADE)
        commentpost=models.ForeignKey(teacherupload, related_name='comments', on_delete=models.CASCADE)
        name=models.CharField(max_length=120)
        body=RichTextUploadingField()
        date=models.DateTimeField(default=datetime.now)
        parent=models.ForeignKey('self', null=True , blank=True , on_delete=models.CASCADE, related_name='replies')

        @property
        def children(self):
                return Comment.objects.filter(parent=self).reverse()

        @property
        def is_parent(self):
                if self.parent is None:
                        return True
                return False   

class Syllabus(models.Model):
        scheme=RichTextUploadingField()
        textbooks=RichTextUploadingField()
        syllabus_subject=models.CharField(max_length=60,choices=SUBJECTS,default="")
        syllabus_class=models.CharField(max_length=60,choices=CLASS,default="")
        syllabus_term=models.CharField(max_length=60,choices=TERM,default="")
# class SyllabusUpload(models.Model):
#         scheme=RichTextUploadingField()
#         textbooks=RichTextUploadingField()
#         syllabus_class=models.CharField(max_length=60,choices=CLASS,default="")
#         syllabus_term=models.CharField(max_length=60,choices=TERM,default="")

class Login(models.Model):
        name=models.CharField(max_length=120)
        school_class=models.CharField(max_length=120)


class schedule(models.Model):
        event_name=models.CharField(max_length=240)
        date=models.DateTimeField(default="")
        description=models.TextField(max_length=1200)
        link=models.CharField(max_length=120)

