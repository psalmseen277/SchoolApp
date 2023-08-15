"""myschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from edu import views
from edu.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',selectSubject,name="selectsubject"),
    path("selectsyllabus",selectsyllabus,name="selectsyllabus"),
    path("seesyllabus/<str:syllabus_class>/<str:syllabus_subject>",seesyllabus,name="seesyllabus"),
    path("selectsubject",selectSubject,name="selectsubject"),
    path("selectthisusbject/<str:subjectname>/<str:classname>",selectThisSubject,name="selectthissubject"),
    path("showcontent/<slug:slug>/",showcontent,name="showcontent"),
    path("page_admin/",page_admin,name="page_admin"),
    path("syllabus/<str:syllabus_class>/<str:syllabus_term>",syllabus,name="syllabus"),
    path('signup/',views.signup,name='signup'),
    path('logout_user/',logout_user,name='logout_user'),
    path('login/',views.login_request,name='login'),
    path('ok_delete/',views.ok_delete,name='ok_delete'),
    path('delete_syllabus/<id>',delete_syllabus,name='delete-syllabus'),
    path('delete_comment/<id>',delete_comment,name='delete-comment'),
    path('lectureupdate/<id>',lectureupdate,name='lectureupdate'),
    path('update_syllabus/<id>',update_syllabus,name='update-syllabus'),
    path('update_user/<id>',update_user,name='update-user'),
    path('<int:id>',delete,name='delete'),
    path('deletedetail',deletedetail,name='deletedetail'),
    path('bfordelete',bfordelete,name='bfordelete'),    
    path('showcontent/<slug:slug>/delete/',product_delete_view,name='product-delete'),   
    path('<int:id>',detail,name='detail'), 
    path('remove',remove,name='remove'),  
    path('upload/',upload,name='upload'), 
    path('syllabusupload/',syllabusupload,name='syllabusupload'), 
    path('success/',success,name='success'),
    path('schedule_upload/',schedule_upload,name='schedule_upload'),
    path('schedule_view/',schedule_view,name='schedule_view'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404="edu.views.handler_not_found"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)