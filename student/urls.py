"""formtry URL Configuration

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

from django.urls import path,include
from student import views


urlpatterns = [
    path('',views.signup),
    path('login/',views.login,name="rohit"),
    path('profile/',views.profile,name="profile"),
    path('logout/',views.log__out,name="lgout"),
    path('changepass/',views.change_pass_with_old,name="password"),
    path('changepass1/',views.change_pass_without_old,name="without_old"),
    path('public_blog/',views.public_blog,name="p_blog"),
    path('user_details/<int:id>',views.user_details,name="user_details"),
    path('delete_blog/<int:id>',views.delete_blog,name="delete_blog"),
    path('create_post/',views.create_post,name="create_post"),
    path('edit_blog/<int:id>',views.edit_post,name="edit_blog"),
    path('guest_login/',views.guest_login,name="guest"),
    path('fetch_news/',views.news,name="fetch_news")
]
