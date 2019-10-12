#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:08:00 2019

@author: benpradko
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]