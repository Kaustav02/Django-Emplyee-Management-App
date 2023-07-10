from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/',emp_home),
    path('add/',add_emp),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update/",do_update),
    
]
