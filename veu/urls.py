# -*- coding:utf-8 -*-
# Author:XXX
from django.conf.urls import url, include
from django.urls import path
import sys
import os

sys.path.append("/root/untitled/seven/")
from veu import views
urlpatterns = [
    path(r'add_book$', views.add_book, ),
    path(r'show_books$', views.show_books, ),
]