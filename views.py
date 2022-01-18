from django.shortcuts import render
from django.http import HttpRequest

def imshow():
    return HttpRequest('<h4>Python/<h4')