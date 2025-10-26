from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app1/index.html',{'param1':"Hello World"})

def factorial(request):
    n1 = 5
    n2 = arrayfact(n1)
    return render(request,'app1/index.html',{'param1':n1,'param2': n2})

def fact(n1):
    result = 1
    for i in range(1,1+n1,1):
        result = result * i
    return result

def arrayfact(n1):
    list1 = []
    list2 = []
    result = 1
    for i in range(1,n1+1,1):
        result = fact(i)
        list1.append(result)
        list2.append(i)
    return zip(list2,list1)