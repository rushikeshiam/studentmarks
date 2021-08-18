"""studentinfo URL Configuration

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
from django.urls import path
from student import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login,name='login'),
    path('dologin/', views.dologin,name='dologin'),
    path('', views.show_student,name='show-student'),
    path('show-details/<str:student_id>', views.show_details,name='show-details'),
    path('add-student/', views.add_student,name='add-student'),
    path('add-student-save/', views.add_student_save,name='add-student-save'),
    path('edit-student/<str:student_id>', views.edit_student,name='edit-student'),
    path('edit-student-save/', views.edit_student_save,name='edit-student-save'),
    path('delete-student/<str:student_id>', views.delete_student,name='delete-student'),
    path('search', views.search_box,name='search'),
    path('search-url', views.search_url,name='search-url'),
    path('logout-user/', views.logout_user,name='logout'),
]
