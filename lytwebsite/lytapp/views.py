from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'lytapp/home.html',{'param1':[0,1]})

def about(request):
    return render(request,'lytapp/about.html')

def contact(request):
    return render(request,'lytapp/contact.html')