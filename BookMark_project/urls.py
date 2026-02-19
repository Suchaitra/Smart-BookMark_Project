"""
URL configuration for BookMark_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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





from django.urls import path
from myapp.views import bookmark_list,delete_bookmark,update_bookmark,add_bookmark

urlpatterns = [
    path('', bookmark_list, name='bookmark_list'),
    path('add/', add_bookmark, name='add_bookmark'),
    path('update/<int:id>/', update_bookmark, name='update_bookmark'),
    path('delete/<int:id>/', delete_bookmark, name='delete_bookmark'),
]