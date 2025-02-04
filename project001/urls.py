"""
URL configuration for project001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topic/',display_topic,name='display_topic'),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_topic_by_f/',insert_topic_by_f,name='insert_topic_by_f'),
    path('insert_topic_by_df/',insert_topic_by_df,name='insert_topic_by_df'),
    path('insert_topic_by_mf/',insert_topic_by_mf,name='insert_topic_by_mf'),


    path('display_webpage/',display_webpage,name='display_webpage'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_webpage_by_f/',insert_webpage_by_f,name='insert_webpage_by_f'),
    path('insert_webpage_by_df/',insert_webpage_by_df,name='insert_webpage_by_df'),
    path('insert_webpage_by_mf/',insert_webpage_by_mf,name='insert_webpage_by_mf'),
    
    
    path('display_access/',display_access,name='display_access'),
    path('insert_access/',insert_accessRecords,name='insert_accessRecords'),
    path('insert_access_by_f/',insert_accessRecords_by_f,name='insert_accessRecords_by_f'),
    path('insert_access_by_df/',insert_accessRecords_by_df,name='insert_accessRecords_by_df'),
    path('insert_access_by_mf/',insert_access_by_mf,name='insert_access_by_mf'),

]