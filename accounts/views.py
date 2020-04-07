from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def HomePage(req):
  return render(req, 'accounts/dashboard.html')
  
def ProductsPage(req):
  return HttpResponse("This is the Products Page. Welcome!")

def CustomerPage(req):
  return HttpResponse('This is the customer page.')
