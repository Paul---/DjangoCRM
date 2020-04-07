from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def HomePage(req):
  return render(req, 'accounts/dashboard.html')
  
def ProductsPage(req):
  return render(req, 'accounts/products.html')

def CustomerPage(req):
  return render(req,'accounts/customer.html')
