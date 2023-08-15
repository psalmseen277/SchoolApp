from django.contrib import admin
from .models import teacherupload,Comment,Syllabus,add_comments,schedule
# Register your models here.
admin.site.register(teacherupload) 
admin.site.register(Comment) 
admin.site.register(Syllabus) 
admin.site.register(add_comments) 
admin.site.register(schedule) 